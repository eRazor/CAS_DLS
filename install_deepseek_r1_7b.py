# Minimal tester for DeepSeek-R1-Distill-Qwen-7B in 8-bit with CPU offload
# Run inside conda env `cas_gpu`.
import sys
import traceback
from time import time

REPO = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"

def attempt_load():
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
        import torch
    except Exception:
        traceback.print_exc()
        return 2

    print("Transformers:", getattr(__import__("transformers"), "__version__", "?"))

    try:
        print("Loading tokenizer for", REPO)
        tok = AutoTokenizer.from_pretrained(REPO, use_fast=False)
        print("Tokenizer OK. vocab_size=", getattr(tok, 'vocab_size', None))
    except Exception:
        print("Tokenizer failed")
        traceback.print_exc()
        return 3

    try:
        print("Configuring 8-bit with CPU offload and loading model; this may use system RAM and take a while...")
        bnb_conf = BitsAndBytesConfig(load_in_8bit=True, llm_int8_enable_fp32_cpu_offload=True)
        t0 = time()
        model = AutoModelForCausalLM.from_pretrained(REPO, quantization_config=bnb_conf, device_map='auto', trust_remote_code=True)
        t1 = time()
        print(f"Model loaded in {t1-t0:.1f}s. Model device_map summary: ")
        try:
            from accelerate.utils import get_balanced_memory
            print("balanced memory info available")
        except Exception:
            pass
        # show small device_map
        if hasattr(model, 'device_map'):
            print(model.device_map)

        # run quick generation
        prompt = "Hello from DeepSeek 7B"
        inputs = tok(prompt, return_tensors='pt')
        device = next(model.parameters()).device
        input_ids = inputs.input_ids.to(device)
        print("Generating small sample...")
        out = model.generate(input_ids, max_new_tokens=16)
        print("Generation OK:", tok.decode(out[0], skip_special_tokens=True))
        return 0
    except Exception:
        traceback.print_exc()
        return 4

if __name__ == '__main__':
    rc = attempt_load()
    print("Exit code:", rc)
    sys.exit(rc)
