import importlib, traceback, sys
mods = ['transformers','accelerate','bitsandbytes','flash_attn']
for m in mods:
    try:
        mod = importlib.import_module(m)
        v = getattr(mod, '__version__', None)
        print(f"{m}: OK, __version__={v}")
    except Exception as e:
        print(f"{m}: ERROR -> {e.__class__.__name__}: {e}")
        traceback.print_exc()
        print('---')
sys.exit(0)

