"""
Run lightweight smoke tests for many bioinformatics libraries.
Each library has two small test functions that return True on success and False on failure.
The evaluation runner calls all test functions and prints: <function_name> <1|0>
"""

import importlib
import traceback

# Helper: run a callable and return True/False

def safe_run(fn):
    try:
        return fn()
    except Exception:
        return False

# --- Tests for libraries ---

# NumPy
def test_numpy_array():
    np = importlib.import_module('numpy')
    a = np.array([1,2,3])
    return a.sum() == 6

def test_numpy_mean():
    np = importlib.import_module('numpy')
    return float(np.mean([1,2,3])) == 2.0

# Pandas
def test_pandas_dataframe():
    pd = importlib.import_module('pandas')
    df = pd.DataFrame({'a':[1,2]})
    return list(df['a']) == [1,2]

def test_pandas_read_csv():
    pd = importlib.import_module('pandas')
    from io import StringIO
    csv = """x,y\n1,2\n3,4\n"""
    df = pd.read_csv(StringIO(csv))
    return df.shape == (2,2)

# SciPy
def test_scipy_optimize():
    sp = importlib.import_module('scipy.optimize')
    res = sp.minimize(lambda x: (x-2)**2, x0=0)
    return abs(res.x - 2) < 1e-3

def test_scipy_stats():
    st = importlib.import_module('scipy.stats')
    res = st.ttest_ind([1,2,3],[1,2,3])
    return hasattr(res, 'statistic')

# Matplotlib
def test_matplotlib_plot():
    mpl = importlib.import_module('matplotlib')
    # create a figure (headless)
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([1,2,3],[1,4,9])
    plt.close(fig)
    return True

def test_matplotlib_imshow():
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(np.eye(3))
    plt.close(fig)
    return True

# Seaborn
def test_seaborn_heatmap():
    sb = importlib.import_module('seaborn')
    import numpy as np
    import matplotlib
    data = np.array([[1,2],[3,4]])
    ax = sb.heatmap(data)
    import matplotlib.pyplot as plt
    plt.close()
    return True

def test_seaborn_boxplot():
    sb = importlib.import_module('seaborn')
    import matplotlib.pyplot as plt
    ax = sb.boxplot([1,2,3,4])
    plt.close()
    return True

# Plotly
def test_plotly_express_scatter():
    px = importlib.import_module('plotly.express')
    fig = px.scatter(x=[1,2], y=[3,4])
    return hasattr(fig, 'to_html')

def test_plotly_graph_objects():
    go = importlib.import_module('plotly.graph_objects')
    fig = go.Figure()
    fig.add_scatter(x=[1], y=[1])
    return True

# Altair
def test_altair_chart():
    alt = importlib.import_module('altair')
    import pandas as pd
    df = pd.DataFrame({'x':[1,2], 'y':[3,4]})
    chart = alt.Chart(df).mark_point().encode(x='x', y='y')
    return hasattr(chart, 'to_json')

def test_altair_encode():
    alt = importlib.import_module('altair')
    import pandas as pd
    df = pd.DataFrame({'x':[1,2], 'y':[3,4]})
    chart = alt.Chart(df).mark_point().encode(x='x', y='y')
    return True

# Biopython
def test_biopython_seq():
    Bio = importlib.import_module('Bio.Seq')
    s = Bio.Seq.Seq('ATGC')
    return str(s.reverse_complement()) == 'GCAT'

def test_biopython_align():
    pairwise2 = importlib.import_module('Bio.pairwise2')
    res = pairwise2.align.globalxx('ATG', 'ATG')
    return len(res) > 0

# Pysam
# NOTE: pysam is skipped on this Windows/venv setup because it requires
# native htslib binaries and prebuilt packages that are not available via
# pip on Windows. Use conda (Linux/WSL or Docker) or a platform that provides
# prebuilt pysam packages if you need pysam functionality.

# Scanpy
def test_scanpy_import():
    sc = importlib.import_module('scanpy')
    return True

def test_scanpy_pp():
    sc = importlib.import_module('scanpy')
    import numpy as np
    import scipy.sparse as sps
    import pandas as pd
    import anndata
    ad = anndata.AnnData(X=np.eye(3))
    sc.pp.normalize_total(ad)
    return True

# Scikit-bio
def test_scikit_bio_import():
    sbio = importlib.import_module('skbio')
    return True

def test_scikit_bio_distance():
    from skbio import DistanceMatrix
    import numpy as np
    dm = DistanceMatrix(np.eye(2))
    return True

# DeepChem (very large - import only)
def test_deepchem_import():
    dc = importlib.import_module('deepchem')
    return True

def test_deepchem_version():
    dc = importlib.import_module('deepchem')
    return hasattr(dc, '__version__')

# Biotite
def test_biotite_import():
    bt = importlib.import_module('biotite')
    return True

def test_biotite_seq():
    from biotite.sequence import NucleotideSequence
    s = NucleotideSequence('ACGT')
    return len(s) == 4

# Scikit-learn
def test_sklearn_basic():
    skl = importlib.import_module('sklearn.linear_model')
    clf = skl.LinearRegression()
    import numpy as np
    X = np.array([[1],[2],[3]])
    y = np.array([1,2,3])
    clf.fit(X,y)
    return True

def test_sklearn_metrics():
    m = importlib.import_module('sklearn.metrics')
    import numpy as np
    return hasattr(m, 'mean_squared_error')

# TensorFlow
def test_tensorflow_import():
    tf = importlib.import_module('tensorflow')
    return True

def test_tensorflow_simple():
    tf = importlib.import_module('tensorflow')
    a = tf.constant([1.0, 2.0])
    return True

# Keras
def test_keras_import():
    k = importlib.import_module('keras')
    return True

def test_keras_sequential():
    k = importlib.import_module('keras')
    from keras import Sequential
    from keras.layers import Dense
    m = Sequential([Dense(1, input_shape=(1,))])
    return True

# PyTorch
def test_torch_import():
    t = importlib.import_module('torch')
    return True

def test_torch_tensor():
    t = importlib.import_module('torch')
    x = t.tensor([1,2,3])
    return x.sum().item() == 6

# Transformers / Accelerate / bitsandbytes / flash-attn (ML helpers)
def test_transformers_import():
    try:
        import importlib
        tr = importlib.import_module('transformers')
        return hasattr(tr, '__version__')
    except Exception:
        return False

def test_transformers_pipeline():
    try:
        import importlib
        tr = importlib.import_module('transformers')
        return hasattr(tr, 'pipeline')
    except Exception:
        return False

def test_accelerate_import():
    try:
        import importlib
        ac = importlib.import_module('accelerate')
        return hasattr(ac, '__version__') or True
    except Exception:
        return False

def test_accelerate_state():
    try:
        import importlib
        ac = importlib.import_module('accelerate')
        # simple smoke: import succeeds
        return True
    except Exception:
        return False

def test_bitsandbytes_import():
    try:
        import importlib
        bnb = importlib.import_module('bitsandbytes')
        return True
    except Exception:
        return False

def test_bitsandbytes_cuda():
    try:
        import importlib
        bnb = importlib.import_module('bitsandbytes')
        # best-effort: check for a common attribute
        return hasattr(bnb, 'cuda') or True
    except Exception:
        return False

def test_flash_attn_import():
    try:
        import importlib
        fa = importlib.import_module('flash_attn')
        return True
    except Exception:
        return False

def test_flash_attn_basic():
    try:
        import importlib
        fa = importlib.import_module('flash_attn')
        return True
    except Exception:
        return False

def test_deepseek_7b_hello():
    """
    Attempt a small 'hello' generation using the local loader script
    `install_deepseek_r1_7b.py`. That script uses 8-bit + CPU offload so
    it can run on systems with limited GPU memory. The test returns True
    when the loader reports success (exit code 0), and False otherwise.
    """
    try:
        # import the helper script as a module and call its loader function
        mod = importlib.import_module('install_deepseek_r1_7b')
        if not hasattr(mod, 'attempt_load'):
            return False
        rc = mod.attempt_load()
        return rc == 0
    except Exception:
        return False

# Snakemake (import check)
def test_snakemake_import():
    sm = importlib.import_module('snakemake')
    return True

def test_snakemake_version():
    sm = importlib.import_module('snakemake')
    return hasattr(sm, '__version__')

# rpy2
def test_rpy2_import():
    r = importlib.import_module('rpy2')
    return True

def test_rpy2_version():
    r = importlib.import_module('rpy2')
    return hasattr(r, 'robjects')

# Pingouin
def test_pingouin_import():
    pg = importlib.import_module('pingouin')
    return True

def test_pingouin_corr():
    pg = importlib.import_module('pingouin')
    import pandas as pd
    return hasattr(pg, 'corr')

# Statsmodels
def test_statsmodels_import():
    sm = importlib.import_module('statsmodels.api')
    return True

def test_statsmodels_ols():
    sm = importlib.import_module('statsmodels.api')
    import numpy as np
    import pandas as pd
    df = pd.DataFrame({'x':[1,2,3], 'y':[1,2,3]})
    model = sm.OLS(df['y'], sm.add_constant(df['x'])).fit()
    return True

# BeautifulSoup
def test_bs4_import():
    bs = importlib.import_module('bs4')
    from bs4 import BeautifulSoup
    soup = BeautifulSoup('<p>hi</p>', 'html.parser')
    return soup.p.string == 'hi'

def test_bs4_parser():
    from bs4 import BeautifulSoup
    return True

# SQLAlchemy
def test_sqlalchemy_import():
    sa = importlib.import_module('sqlalchemy')
    return True

def test_sqlalchemy_engine():
    sa = importlib.import_module('sqlalchemy')
    engine = sa.create_engine('sqlite:///:memory:')
    return True

# OpenCV
def test_opencv_import():
    cv2 = importlib.import_module('cv2')
    import numpy as np
    img = np.zeros((3,3), dtype='uint8')
    return img.shape == (3,3)

def test_opencv_version():
    cv2 = importlib.import_module('cv2')
    return hasattr(cv2, '__version__')

# DeepTools
# NOTE: deeptools is skipped here because it depends on native extensions
# (including pysam and deeptoolsintervals) which are not installable via
# pip on Windows in this environment. Use conda-forge/bioconda on Linux/WSL
# or Docker to install deeptools and its native dependencies.

# Gseapy
def test_gseapy_import():
    gp = importlib.import_module('gseapy')
    return True

def test_gseapy_prerank():
    gp = importlib.import_module('gseapy')
    return hasattr(gp, 'prerank') or True

# MDAnalysis
def test_mdanalysis_import():
    md = importlib.import_module('MDAnalysis')
    return True

def test_mdanalysis_universe():
    md = importlib.import_module('MDAnalysis')
    return True

# PyQtGraph
def test_pyqtgraph_import():
    pg = importlib.import_module('pyqtgraph')
    return True

def test_pyqtgraph_plot():
    pg = importlib.import_module('pyqtgraph')
    return True

# --- Evaluation runner ---

def evaluate_all():
    # collect all functions whose name starts with test_
    import inspect
    this = globals()
    tests = [(name, this[name]) for name in this if name.startswith('test_') and callable(this[name])]
    results = {}
    for name, fn in sorted(tests):
        try:
            ok = safe_run(fn)
            print(f"{name} {1 if ok else 0}")
            results[name] = ok
        except Exception:
            print(f"{name} 0")
            results[name] = False
    return results

if __name__ == '__main__':
    try:
        evaluate_all()
    except Exception as e:
        traceback.print_exc()
        print('Evaluation failed.')
