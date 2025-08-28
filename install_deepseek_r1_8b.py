# Minimal installer/tester for DeepSeek-R1-Distill-Llama-8B 8-bit
# Attempts to install/verify required packages and to load tokenizer + model in 8-bit.
# Run inside the `cas_gpu` conda env.

import sys
import traceback

REPO = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"

def try_imports():
    names = ["transformers", "bitsandbytes", "safetensors", "huggingface_hub", "accelerate"]
    ok = {}
    for n in names:
        try:
            __import__(n)
            ok[n] = True
        except Exception as e:
            ok[n] = False
    return ok


def attempt_load():
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
        import torch
    except Exception as e:
        print("IMPORT_ERROR", file=sys.stderr)
        traceback.print_exc()
        return 2

    print("Transformers version:", getattr(__import__("transformers"), "__version__", "?"))

    try:
        print("Downloading tokenizer/config for %s" % REPO)
        tok = AutoTokenizer.from_pretrained(REPO, use_fast=False)
        print("Tokenizer loaded. vocab_size=", getattr(tok, 'vocab_size', None))
    except Exception as e:
        print("TOKENIZER_ERROR", file=sys.stderr)
        traceback.print_exc()
        return 3

    try:
        print("Preparing 8-bit quantization config and attempting to load model (this may OOM or take a long time)...")
        bnb_config = BitsAndBytesConfig(load_in_8bit=True)
        # Use device_map='auto' and trust_remote_code in case model uses custom code
        model = AutoModelForCausalLM.from_pretrained(REPO, quantization_config=bnb_config, device_map='auto', trust_remote_code=True)
        print("Model loaded. Summary:")
        print(model)
        # simple forward
        prompt = "Hello"
        input_ids = tok(prompt, return_tensors='pt').input_ids.to(next(model.parameters()).device)
        out = model.generate(input_ids, max_new_tokens=16)
        print("Generation OK:", tok.decode(out[0], skip_special_tokens=True))
        return 0
    except Exception as e:
        print("MODEL_LOAD_ERROR", file=sys.stderr)
        traceback.print_exc()
        return 4


if __name__ == '__main__':
    print("Checking installed packages...")
    res = try_imports()
    for k,v in res.items():
        print(k, 'installed' if v else 'MISSING')

    rc = attempt_load()
    print("Exit code:", rc)
    sys.exit(rc)
