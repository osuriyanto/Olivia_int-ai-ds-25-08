
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns

# Page config
st.set_page_config(
    page_title = 'Not A Spam',
    page_icon="📊",
    layout = 'wide'
)

# Title
st.title("Statistical Diagrams")
st.markdown("Interactive view of different types of statistical distribution.")

#sidebar items
random_seed = st.sidebar.number_input("Random seed", value = 42, min_value = 1)
size_samples = st.sidebar.number_input("Size samples (100 to 100000)", value = 10000, min_value=100)
loc = st.sidebar.number_input("Loc (2 to 9)", min_value = 2, max_value = 9, value=5)
scale = st.sidebar.number_input("Scale (std dev; 1 to 2)", min_value = 1, max_value = 2, value=1)
plot_range = st.sidebar.slider("Range for random.randint and random.uniform", min_value = 0, max_value = 10, value=(0,10))

# Load data
@st.cache_data

def load_data(random_seed, size_samples, loc, scale, plot_range):
    np.random.seed(random_seed)
    df = pd.DataFrame({
        'random_normal' : np.random.normal(loc, scale, size_samples).round(2),
        'random_lognormal' : np.random.lognormal(loc, scale, size_samples).round(2),
        'random_exponential' : np.random.exponential(scale,size_samples).round(2),
        'random_poisson' : np.random.poisson(loc,size_samples),
        'random_randint' : np.random.randint(plot_range[0], plot_range[1], size_samples),
        'random_uniform' : np.random.uniform(plot_range[0], plot_range[1], size_samples).round(2)
    })
    return df

distribution_df = load_data(random_seed, size_samples, loc, scale, plot_range)

# Row 1: Top plots
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("np.random.normal()")
    fig, ax = plt.subplots(figsize = (5,4))
    ax.hist(distribution_df['random_normal'], bins=40, color='steelblue', alpha=0.7, label='normal dist.')
    ax.set_xlabel(None)
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.caption(f"numpy.random.normal(loc= {loc}, scale= {scale}, size= {size_samples})")
    st.caption("[Docs] https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html")

with col2:
    st.subheader("np.random.lognormal()")
    fig, ax = plt.subplots(figsize = (5,4))
    ax.hist(distribution_df['random_lognormal'], bins=40, color='orange', alpha=0.7, label='lognormal dist.')
    ax.set_xlabel(None)
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.caption(f"numpy.random.lognormal(loc= {loc}, scale= {scale}, size= {size_samples})")
    st.caption("[Docs] https://numpy.org/doc/stable/reference/random/generated/numpy.random.lognormal.html")

with col3:
    st.subheader("np.random.exponential()")
    fig, ax = plt.subplots(figsize = (5,4))
    ax.hist(distribution_df['random_exponential'], bins=40, color = 'red', alpha=0.7, label='exponential dist.')
    ax.set_xlabel(None)
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.caption(f"numpy.random.exponential(scale= {scale}, size= {size_samples})")
    st.caption("[Docs] https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html")

# Row 2: Bottom plots
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("np.random.poisson()")
    fig, ax = plt.subplots(figsize = (5,4))
    ax.hist(distribution_df['random_poisson'], bins=40, color = 'red', alpha=0.7, label='poisson dist.')
    ax.set_xlabel(None)
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.caption(f"numpy.random.poisson(lam= {loc}, size= {size_samples})")
    st.caption("[Docs] https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html")

with col2:
    st.subheader("np.random.randint()")
    fig, ax = plt.subplots(figsize = (5,4))
    bins = np.arange(plot_range[0], plot_range[1]+1)
    ax.hist(distribution_df['random_randint'], bins=bins, color = 'orange', alpha=0.7, label='randint dist.')
    ax.set_xlabel(None)
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.caption(f"numpy.random.randint(low= {plot_range[0]}, high= {plot_range[1]}, size= {size_samples})")
    st.caption("[Docs] https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html")

with col3:
    st.subheader("np.random.uniform()")
    fig, ax = plt.subplots(figsize = (5,4))
    ax.hist(distribution_df['random_uniform'], bins=40, color = 'limegreen', alpha=0.7, label='uniform dist.')
    ax.set_xlabel(None)
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.caption(f"numpy.random.uniform(low= {plot_range[0]}, high= {plot_range[1]}, size= {size_samples})")
    st.caption("[Docs] https://numpy.org/doc/2.3/reference/random/generated/numpy.random.uniform.html")

# Footer
st.markdown("---")
st.caption("Dashboard is created with Streamlit.")
