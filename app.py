import os
import time
import csv
from pathlib import Path
from datetime import datetime

import torch
import gradio as gr
from diffusers import StableDiffusionPipeline

import webbrowser
import threading

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "stable-diffusion-v1-5"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_PATH = LOG_DIR / "perf_log.csv"

def append_log(row: dict):
    write_header = not LOG_PATH.exists()
    with LOG_PATH.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=row.keys())
        if write_header:
            w.writeheader()
        w.writerow(row)

def load_pipeline():
    if not MODEL_DIR.exists():
        raise RuntimeError(
            f"Modellordner nicht gefunden: {MODEL_DIR}\n"
            "Bitte Modell vorher herunterladen (siehe README)."
        )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32

    pipe = StableDiffusionPipeline.from_pretrained(
        str(MODEL_DIR),
        torch_dtype=dtype,
        local_files_only=True
    )

    if device == "cuda":
        pipe = pipe.to("cuda")
        try:
            pipe.enable_xformers_memory_efficient_attention()
        except Exception:
            pass
    else:
        pipe = pipe.to("cpu")

    return pipe, device

PIPE, DEVICE = load_pipeline()

def generate(prompt: str, steps: int, guidance: float, seed: int):
    if not prompt or not prompt.strip():
        raise gr.Error("Bitte einen Prompt eingeben.")

    gen = torch.Generator(device="cuda" if DEVICE == "cuda" else "cpu")
    if seed >= 0:
        gen = gen.manual_seed(seed)

    if DEVICE == "cuda":
        torch.cuda.reset_peak_memory_stats()
        torch.cuda.synchronize()

    t0 = time.perf_counter()
    image = PIPE(
        prompt=prompt,
        num_inference_steps=int(steps),
        guidance_scale=float(guidance),
        generator=gen
    ).images[0]
    if DEVICE == "cuda":
        torch.cuda.synchronize()
    t1 = time.perf_counter()

    vram_peak_mb = None
    if DEVICE == "cuda":
        vram_peak_mb = torch.cuda.max_memory_allocated() / (1024 * 1024)

    row = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "device": DEVICE,
        "steps": int(steps),
        "guidance": float(guidance),
        "seed": int(seed),
        "time_ms": round((t1 - t0) * 1000, 2),
        "vram_peak_mb": round(vram_peak_mb, 1) if vram_peak_mb is not None else None,
        "prompt_len": len(prompt),
    }
    append_log(row)

    return image

with gr.Blocks(title="Bildgenerierung (Diffusers)") as demo:
    gr.Markdown("# Bildgenerierung (Text → Bild)\nPrompt eingeben → Generate.")

    prompt = gr.Textbox(label="Prompt", placeholder="z.B. a photo of a red bicycle in the rain, cinematic lighting")
    with gr.Row():
        steps = gr.Slider(10, 50, value=25, step=1, label="Steps")
        guidance = gr.Slider(1.0, 12.0, value=7.5, step=0.5, label="Guidance")
        seed = gr.Number(value=-1, precision=0, label="Seed (-1 = zufällig)")

    btn = gr.Button("Generate")
    out = gr.Image(label="Ergebnis")

    btn.click(generate, inputs=[prompt, steps, guidance, seed], outputs=out)

def open_browser():
    webbrowser.open("http://127.0.0.1:7861")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    demo.launch(server_name="127.0.0.1", server_port=7861, share=False, inbrowser=False, prevent_thread_lock=False)