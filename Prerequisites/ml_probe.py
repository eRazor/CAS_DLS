import traceback

for name in ('transformers','accelerate','bitsandbytes','flash_attn'):
    try:
        m = __import__(name)
        print(name, 'import OK,', getattr(m, '__version__', 'unknown'))
    except Exception as e:
        print(name, 'import FAILED:', e.__class__.__name__, str(e))
        traceback.print_exc()


        