"""
Bootstrapping: A Comprehensive Guide and Implementation

Bootstrapping is a powerful statistical resampling technique that allows us to:
1. Estimate the sampling distribution of a statistic
2. Calculate confidence intervals
3. Perform hypothesis testing
4. Assess model uncertainty

Key Concept: Bootstrap sampling involves repeatedly sampling WITH REPLACEMENT 
from the original dataset to create many "bootstrap samples" of the same size.

APPLICATIONS
Bootstrap is useful for:
• Estimating confidence intervals when theoretical distributions are unknown
• Model validation and uncertainty quantification
• Bias correction of estimators
• Hypothesis testing with non-parametric methods
• Feature importance assessment in machine learning
• Time series analysis with block bootstrap
    "\n5. ADVANTAGES AND LIMITATIONS
Advantages:
• Non-parametric: No assumptions about underlying distribution
• Versatile: Works with any statistic
• Simple to implement and understand
• Provides uncertainty estimates
    \nLimitations:
• Computationally intensive
• Assumes original sample is representative
• May not work well with very small samples
• Can be biased for extreme statistics

SUMMARY
Bootstrapping is a fundamental technique in modern statistics and machine learning.
It provides a way to estimate the sampling distribution of any statistic
without making strong parametric assumptions about the underlying population.
This makes it invaluable for uncertainty quantification and robust inference.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')


class BootstrapAnalyzer:
    """
    A comprehensive class for performing various types of bootstrap analysis
    """
    
    def __init__(self, data, n_bootstrap=1000, random_state=42):
        """
        Initialize the Bootstrap Analyzer
        
        Parameters:
        -----------
        data : array-like
            The original dataset
        n_bootstrap : int
            Number of bootstrap samples to generate
        random_state : int
            Random seed for reproducibility
        """
        self.data = np.array(data)
        self.n_bootstrap = n_bootstrap
        self.random_state = random_state
        np.random.seed(random_state)
        
    def basic_bootstrap(self, statistic_func=np.mean):
        """
        Perform basic bootstrap resampling
        
        Parameters:
        -----------
        statistic_func : function
            Function to calculate the statistic (default: mean)
            
        Returns:
        --------
        bootstrap_statistics : array
            Array of bootstrap statistics
        """
        bootstrap_stats = []
        n = len(self.data)
        
        for i in range(self.n_bootstrap):
            # Sample with replacement
            bootstrap_sample = np.random.choice(self.data, size=n, replace=True)
            # Calculate statistic
            stat = statistic_func(bootstrap_sample)
            bootstrap_stats.append(stat)
            
        return np.array(bootstrap_stats)
    
    def confidence_interval(self, statistic_func=np.mean, confidence_level=0.95):
        """
        Calculate bootstrap confidence interval
        
        Parameters:
        -----------
        statistic_func : function
            Function to calculate the statistic
        confidence_level : float
            Confidence level (e.g., 0.95 for 95% CI)
            
        Returns:
        --------
        tuple : (lower_bound, upper_bound, bootstrap_stats)
        """
        bootstrap_stats = self.basic_bootstrap(statistic_func)
        
        alpha = 1 - confidence_level
        lower_percentile = (alpha/2) * 100
        upper_percentile = (1 - alpha/2) * 100
        
        lower_bound = np.percentile(bootstrap_stats, lower_percentile)
        upper_bound = np.percentile(bootstrap_stats, upper_percentile)
        
        return lower_bound, upper_bound, bootstrap_stats
    
    def bias_correction(self, statistic_func=np.mean):
        """
        Calculate bias-corrected bootstrap estimate

        Parameters:
        -----------
        statistic_func : function
            Function to calculate the statistic

        Returns:
        --------
        dict : Contains original estimate, bootstrap mean, bias, and corrected estimate
        """
        # Original statistic
        original_stat = statistic_func(self.data)

        # Bootstrap statistics
        bootstrap_stats = self.basic_bootstrap(statistic_func)
        bootstrap_mean = np.mean(bootstrap_stats)

        # Bias calculation
        bias = bootstrap_mean - original_stat

        # Bias-corrected estimate
        corrected_estimate = original_stat - bias

        return {
            'original_estimate': original_stat,
            'bootstrap_mean': bootstrap_mean,
            'bias': bias,
            'corrected_estimate': corrected_estimate,
            'bootstrap_stats': bootstrap_stats
        }

    def get_bootstrap_data(self, statistic_func=np.mean, confidence_level=0.95):
        """
        Get bootstrap data for visualization

        Parameters:
        -----------
        statistic_func : function
            Function to calculate the statistic (default: mean)
        confidence_level : float
            Confidence level for CI (default: 0.95)

        Returns:
        -----------
        dict : Dictionary containing all data needed for visualization
        """
        bootstrap_stats = self.basic_bootstrap(statistic_func)
        original_stat = statistic_func(self.data)
        bootstrap_lower, bootstrap_upper, _ = self.confidence_interval(statistic_func, confidence_level)

        # Theoretical calculations (for mean)
        sample_mean = np.mean(self.data)
        sample_std = np.std(self.data, ddof=1)
        se_mean = sample_std / np.sqrt(len(self.data))
        t_critical = stats.t.ppf((1 + confidence_level) / 2, df=len(self.data)-1)
        theoretical_lower = sample_mean - t_critical * se_mean
        theoretical_upper = sample_mean + t_critical * se_mean

        return {
            'original_data': self.data,
            'bootstrap_stats': bootstrap_stats,
            'original_stat': original_stat,
            'bootstrap_mean': np.mean(bootstrap_stats),
            'bootstrap_std': np.std(bootstrap_stats),
            'bootstrap_lower': bootstrap_lower,
            'bootstrap_upper': bootstrap_upper,
            'theoretical_lower': theoretical_lower,
            'theoretical_upper': theoretical_upper,
            'sample_mean': sample_mean,
            'sample_std': sample_std,
            'se_mean': se_mean,
            'confidence_level': confidence_level,
            'n_bootstrap': self.n_bootstrap,
            'statistic_func': statistic_func
        }

    def get_confidence_interval_comparison_data(self, statistic_func=np.mean, confidence_levels=[0.90, 0.95, 0.99]):
        """
        Get data for confidence interval comparison across different confidence levels

        Parameters:
        -----------
        statistic_func : function
            Function to calculate the statistic (default: mean)
        confidence_levels : list
            List of confidence levels to compare

        Returns:
        -----------
        dict : Dictionary containing CI comparison data
        """
        original_stat = statistic_func(self.data)
        bootstrap_cis = []
        theoretical_cis = []

        for cl in confidence_levels:
            # Bootstrap CI
            boot_lower, boot_upper, _ = self.confidence_interval(statistic_func, cl)
            bootstrap_cis.append((boot_lower, boot_upper))

            # Theoretical CI (for mean)
            if statistic_func == np.mean:
                sample_mean = np.mean(self.data)
                sample_std = np.std(self.data, ddof=1)
                se_mean = sample_std / np.sqrt(len(self.data))
                t_critical = stats.t.ppf((1 + cl) / 2, df=len(self.data)-1)
                theo_lower = sample_mean - t_critical * se_mean
                theo_upper = sample_mean + t_critical * se_mean
                theoretical_cis.append((theo_lower, theo_upper))
            else:
                theoretical_cis.append((np.nan, np.nan))

        return {
            'original_stat': original_stat,
            'confidence_levels': confidence_levels,
            'bootstrap_cis': bootstrap_cis,
            'theoretical_cis': theoretical_cis,
            'sample_size': len(self.data),
            'statistic_func': statistic_func
        }
    
class BootstrapVisualizer:
    """
    Visualization class for bootstrap analysis results
    """
    @staticmethod
    def plot_bootstrap_distribution(bootstrap_data, title="Bootstrap Distribution", save_path="bootstrap_distribution.png"):
        """
        Plot the bootstrap distribution

        Parameters:
        -----------
        bootstrap_data : dict
            Data dictionary from BootstrapAnalyzer.get_bootstrap_data()
        title : str
            Plot title
        """
        plt.figure(figsize=(10, 6))
        plt.hist(bootstrap_data['bootstrap_stats'], bins=50, alpha=0.7, density=True,
                color='skyblue', edgecolor='black')
        plt.axvline(bootstrap_data['original_stat'], color='red', linestyle='--', linewidth=2,
                   label=f'Original Statistic: {bootstrap_data["original_stat"]:.3f}')
        plt.axvline(bootstrap_data['bootstrap_mean'], color='green', linestyle='--', linewidth=2,
                   label=f'Bootstrap Mean: {bootstrap_data["bootstrap_mean"]:.3f}')

        plt.xlabel('Statistic Value')
        plt.ylabel('Density')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show(block=False)

        # Save figure if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Figure saved to: {save_path}")

    @staticmethod
    def plot_data_and_bootstrap(bootstrap_data, title="Data and Bootstrap", save_path="data_bootstrap.png"):
        """
        Create side-by-side plots of initial data and bootstrap results

        Parameters:
        -----------
        bootstrap_data : dict
            Data dictionary from BootstrapAnalyzer.get_bootstrap_data()
        save_path : str, optional
            Path to save the figure
        """
        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Plot 1: Initial Data Distribution
        ax1.hist(bootstrap_data['original_data'], bins=30, alpha=0.7, color='lightcoral',
                edgecolor='black', density=True)
        ax1.axvline(np.mean(bootstrap_data['original_data']), color='red', linestyle='--', linewidth=2,
                   label=f'Mean: {np.mean(bootstrap_data["original_data"]):.3f}')
        ax1.axvline(np.median(bootstrap_data['original_data']), color='blue', linestyle='--', linewidth=2,
                   label=f'Median: {np.median(bootstrap_data["original_data"]):.3f}')
        ax1.set_xlabel('Data Values')
        ax1.set_ylabel('Density')
        ax1.set_title('Initial Data Distribution')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Plot 2: Bootstrap Distribution
        ax2.hist(bootstrap_data['bootstrap_stats'], bins=50, alpha=0.7, color='skyblue',
                edgecolor='black', density=True)
        ax2.axvline(bootstrap_data['original_stat'], color='red', linestyle='--', linewidth=2,
                   label=f'Original {bootstrap_data["statistic_func"].__name__}: {bootstrap_data["original_stat"]:.3f}')
        ax2.axvline(bootstrap_data['bootstrap_mean'], color='green', linestyle='--', linewidth=2,
                   label=f'Bootstrap Mean: {bootstrap_data["bootstrap_mean"]:.3f}')

        # Add confidence interval as shaded region
        ax2.axvspan(bootstrap_data['bootstrap_lower'], bootstrap_data['bootstrap_upper'], alpha=0.2, color='orange',
                   label=f'{bootstrap_data["confidence_level"]*100:.0f}% CI: [{bootstrap_data["bootstrap_lower"]:.3f}, {bootstrap_data["bootstrap_upper"]:.3f}]')

        ax2.set_xlabel(f'Bootstrap {bootstrap_data["statistic_func"].__name__.capitalize()} Values')
        ax2.set_ylabel('Density')
        ax2.set_title(f'Bootstrap Distribution ({bootstrap_data["n_bootstrap"]} samples)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        plt.title(title)
        plt.tight_layout()
        plt.show(block=False)

        # Save figure if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Figure saved to: {save_path}")

        # Print summary statistics
        print(f"\n--- Summary Statistics ---")
        print(f"Original data size: {len(bootstrap_data['original_data'])}")
        print(f"Original {bootstrap_data['statistic_func'].__name__}: {bootstrap_data['original_stat']:.3f}")
        print(f"Bootstrap {bootstrap_data['statistic_func'].__name__} (mean): {bootstrap_data['bootstrap_mean']:.3f}")
        print(f"Bootstrap {bootstrap_data['statistic_func'].__name__} (std): {bootstrap_data['bootstrap_std']:.3f}")
        print(f"{bootstrap_data['confidence_level']*100:.0f}% Confidence Interval: [{bootstrap_data['bootstrap_lower']:.3f}, {bootstrap_data['bootstrap_upper']:.3f}]")

    @staticmethod
    def plot_bootstrap_vs_theoretical(bootstrap_data,title="Bootstrap vs Theoretical",  save_path="bootstrap_vs_theoretical.png"):
        """
        Plot bootstrap distribution vs theoretical distribution

        Parameters:
        -----------
        bootstrap_data : dict
            Data dictionary from BootstrapAnalyzer.get_bootstrap_data()
        save_path : str, optional
            Path to save the figure
        """
        # Create theoretical normal distribution curve
        x_theory = np.linspace(np.min(bootstrap_data['bootstrap_stats']),
                              np.max(bootstrap_data['bootstrap_stats']), 1000)

        # For mean statistic, theoretical distribution is normal with mean=sample_mean, std=se_mean
        if bootstrap_data['statistic_func'] == np.mean:
            y_theory = stats.norm.pdf(x_theory, bootstrap_data['sample_mean'], bootstrap_data['se_mean'])
        else:
            y_theory = None

        plt.figure(figsize=(12, 8))

        # Plot bootstrap histogram
        plt.hist(bootstrap_data['bootstrap_stats'], bins=50, alpha=0.7, color='skyblue',
                edgecolor='black', density=True, label='Bootstrap Distribution')

        # Plot theoretical distribution if available
        if y_theory is not None:
            plt.plot(x_theory, y_theory, 'r-', linewidth=3, label='Theoretical Normal Distribution')

        # Add vertical lines for statistics
        plt.axvline(bootstrap_data['original_stat'], color='red', linestyle='--', linewidth=2,
                   label=f'Original {bootstrap_data["statistic_func"].__name__}: {bootstrap_data["original_stat"]:.3f}')
        plt.axvline(bootstrap_data['bootstrap_mean'], color='green', linestyle='--', linewidth=2,
                   label=f'Bootstrap Mean: {bootstrap_data["bootstrap_mean"]:.3f}')

        # Add confidence intervals
        plt.axvspan(bootstrap_data['bootstrap_lower'], bootstrap_data['bootstrap_upper'], alpha=0.2, color='blue',
                   label=f'Bootstrap {bootstrap_data["confidence_level"]*100:.0f}% CI')
        plt.axvspan(bootstrap_data['theoretical_lower'], bootstrap_data['theoretical_upper'], alpha=0.2, color='orange',
                   label=f'Theoretical {bootstrap_data["confidence_level"]*100:.0f}% CI')

        plt.xlabel(f'{bootstrap_data["statistic_func"].__name__.capitalize()} Value')
        plt.ylabel('Density')
        plt.title(f'Bootstrap vs Theoretical Distribution\n({bootstrap_data["n_bootstrap"]} bootstrap samples)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.title(title)
        plt.tight_layout()
        plt.show(block=False)

        # Save figure if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Figure saved to: {save_path}")



        # Print comparison
        print(f"\n--- Bootstrap vs Theoretical Comparison ---")
        print(f"Original {bootstrap_data['statistic_func'].__name__}: {bootstrap_data['original_stat']:.3f}")
        print(f"Bootstrap {bootstrap_data['confidence_level']*100:.0f}% CI: [{bootstrap_data['bootstrap_lower']:.3f}, {bootstrap_data['bootstrap_upper']:.3f}]")
        print(f"Theoretical {bootstrap_data['confidence_level']*100:.0f}% CI: [{bootstrap_data['theoretical_lower']:.3f}, {bootstrap_data['theoretical_upper']:.3f}]")
        print(f"CI width difference: {abs((bootstrap_data['bootstrap_upper'] - bootstrap_data['bootstrap_lower']) - (bootstrap_data['theoretical_upper'] - bootstrap_data['theoretical_lower'])):.3f}")

    @staticmethod
    def plot_confidence_interval_comparison(ci_comparison_data,title="Confidence Interval Comparison",  save_path="confidence_interval_comparison.png"):
        """
        Plot confidence interval comparison across different confidence levels

        Parameters:
        -----------
        ci_comparison_data : dict
            Data dictionary from BootstrapAnalyzer.get_confidence_interval_comparison_data()
        save_path : str, optional
            Path to save the figure
        """
        # Create plot
        fig, ax = plt.subplots(figsize=(12, 8))

        # Plot confidence intervals
        y_positions = np.arange(len(ci_comparison_data['confidence_levels']))

        for i, (cl, (boot_lower, boot_upper), (theo_lower, theo_upper)) in enumerate(zip(
            ci_comparison_data['confidence_levels'],
            ci_comparison_data['bootstrap_cis'],
            ci_comparison_data['theoretical_cis']
        )):
            # Bootstrap CI
            ax.plot([boot_lower, boot_upper], [i, i], 'o-', color='blue', linewidth=3, markersize=8,
                   label='Bootstrap CI' if i == 0 else "")
            ax.plot([boot_lower, boot_upper], [i, i], color='blue', linewidth=8, alpha=0.3)

            # Theoretical CI (if available)
            if not np.isnan(theo_lower):
                ax.plot([theo_lower, theo_upper], [i+0.2, i+0.2], 's-', color='red', linewidth=3, markersize=8,
                       label='Theoretical CI' if i == 0 else "")
                ax.plot([theo_lower, theo_upper], [i+0.2, i+0.2], color='red', linewidth=8, alpha=0.3)

        # Add original statistic line
        ax.axvline(ci_comparison_data['original_stat'], color='green', linestyle='--', linewidth=2,
                  label=f'Original {ci_comparison_data["statistic_func"].__name__}: {ci_comparison_data["original_stat"]:.3f}')

        # Formatting
        ax.set_yticks(y_positions)
        ax.set_yticklabels([f'{cl*100:.0f}%' for cl in ci_comparison_data['confidence_levels']])
        ax.set_xlabel(f'{ci_comparison_data["statistic_func"].__name__.capitalize()} Value')
        ax.set_title('Confidence Interval Comparison: Bootstrap vs Theoretical')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.title(title)
        plt.tight_layout()
        

        # Save figure if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Figure saved to: {save_path}")

        plt.show(block=True)

        # Print detailed comparison
        # print(f"\n--- Confidence Interval Comparison ---")
        print(f"Original {ci_comparison_data['statistic_func'].__name__}: {ci_comparison_data['original_stat']:.3f}")
        print(f"Sample size: {ci_comparison_data['sample_size']}")
        for cl, (boot_lower, boot_upper), (theo_lower, theo_upper) in zip(
            ci_comparison_data['confidence_levels'],
            ci_comparison_data['bootstrap_cis'],
            ci_comparison_data['theoretical_cis']
        ):
            # print(f"\n{cl*100:.0f}% Confidence Level:")
            print(f"  Bootstrap CI: [{boot_lower:.3f}, {boot_upper:.3f}] (width: {boot_upper-boot_lower:.3f})")
            if not np.isnan(theo_lower):
                print(f"  Theoretical CI: [{theo_lower:.3f}, {theo_upper:.3f}] (width: {theo_upper-theo_lower:.3f})")
                print(f"  Difference: {abs((boot_upper-boot_lower) - (theo_upper-theo_lower)):.3f}")


class ModelBootstrap:
    """
    Bootstrap methods for machine learning models
    """
    
    def __init__(self, X, y, model_class=LinearRegression, n_bootstrap=100, random_state=42):
        """
        Initialize Model Bootstrap
        
        Parameters:
        -----------
        X : array-like
            Feature matrix
        y : array-like
            Target variable
        model_class : class
            Machine learning model class
        n_bootstrap : int
            Number of bootstrap samples
        random_state : int
            Random seed
        """
        self.X = np.array(X)
        self.y = np.array(y)
        self.model_class = model_class
        self.n_bootstrap = n_bootstrap
        self.random_state = random_state
        np.random.seed(random_state)
        
    def bootstrap_model_predictions(self, X_test):
        """
        Generate bootstrap predictions for uncertainty estimation
        
        Parameters:
        -----------
        X_test : array-like
            Test features
            
        Returns:
        --------
        predictions : array
            Bootstrap predictions (n_bootstrap x n_test_samples)
        """
        X_test = np.array(X_test)
        n_samples = len(self.X)
        predictions = []
        
        for i in range(self.n_bootstrap):
            # Bootstrap sample indices
            bootstrap_indices = np.random.choice(n_samples, size=n_samples, replace=True)
            
            # Bootstrap sample
            X_bootstrap = self.X[bootstrap_indices]
            y_bootstrap = self.y[bootstrap_indices]
            
            # Fit model and predict
            model = self.model_class()
            model.fit(X_bootstrap, y_bootstrap)
            pred = model.predict(X_test)
            predictions.append(pred)
            
        return np.array(predictions)
    
    def prediction_intervals(self, X_test, confidence_level=0.95):
        """
        Calculate prediction intervals using bootstrap
        
        Parameters:
        -----------
        X_test : array-like
            Test features
        confidence_level : float
            Confidence level
            
        Returns:
        --------
        dict : Contains mean predictions and confidence intervals
        """
        predictions = self.bootstrap_model_predictions(X_test)
        
        alpha = 1 - confidence_level
        lower_percentile = (alpha/2) * 100
        upper_percentile = (1 - alpha/2) * 100
        
        mean_pred = np.mean(predictions, axis=0)
        lower_bound = np.percentile(predictions, lower_percentile, axis=0)
        upper_bound = np.percentile(predictions, upper_percentile, axis=0)
        
        return {
            'mean_prediction': mean_pred,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound,
            'all_predictions': predictions
        }

def demonstrate_bootstrapping():
    """
    Comprehensive demonstration of bootstrapping techniques
    """
    print("=" * 60)
    print("BOOTSTRAPPING DEMONSTRATION")
    print("=" * 60)
    
    true_mean = 200
    true_std = 30
    sample_size = 100
    confidence_interval = 0.95

    # Generate sample data
    np.random.seed(42)
    sample_data = np.random.normal(true_mean, true_std, sample_size)  



    """
    Compare bootstrap results with theoretical results
    """
    # Theoretical confidence interval for mean
    sample_mean = np.mean(sample_data)
    sample_std = np.std(sample_data, ddof=1)
    se_mean = sample_std / np.sqrt(sample_size)
    
    # 95% CI using t-distribution
    t_critical = stats.t.ppf(0.975, df=sample_size-1)
    theoretical_lower = sample_mean - t_critical * se_mean
    theoretical_upper = sample_mean + t_critical * se_mean
    
    # Bootstrap confidence interval
    bootstrap_analyzer = BootstrapAnalyzer(sample_data, n_bootstrap=sample_size)
    
    BootstrapVisualizer.plot_bootstrap_distribution(bootstrap_analyzer.get_bootstrap_data(np.mean, confidence_interval))

    bootstrap_lower, bootstrap_upper, _ = bootstrap_analyzer.confidence_interval(np.mean, confidence_interval)


    print(f"True population mean: {true_mean}")
    print(f"Target Size: {sample_size}")
    print(f"Original sample size: {len(sample_data)}")   
    print(f"Original sample mean: {sample_mean:.3f}")
    print(f"Original sample std: {sample_std:.3f}")
    


    print("\n" + "=" * 60)
    print("BOOTSTRAP vs THEORETICAL COMPARISON")
    print("=" * 60)

    print(f"\nTheoretical 95% CI: [{theoretical_lower:.3f}, {theoretical_upper:.3f}]")
    print(f"Bootstrap 95% CI:   [{bootstrap_lower:.3f}, {bootstrap_upper:.3f}]")
    print(f"CI width difference: {abs((bootstrap_upper - bootstrap_lower) - (theoretical_upper - theoretical_lower)):.3f}")
    
    # Check if true mean is captured
    theoretical_captures = theoretical_lower <= true_mean <= theoretical_upper
    bootstrap_captures = bootstrap_lower <= true_mean <= bootstrap_upper
    
    print(f"\nTrue mean captured by theoretical CI: {theoretical_captures}")
    print(f"True mean captured by bootstrap CI: {bootstrap_captures}")


    # Initialize bootstrap analyzer
    
    # Bootstrap confidence interval for mean
    lower, upper, bootstrap_means = bootstrap_analyzer.confidence_interval(np.mean, confidence_interval)
    # print(f"\n95% Bootstrap Confidence Interval for Mean:")
    print(f"Lower bound: {lower:.3f}")
    print(f"Upper bound: {upper:.3f}")
    print(f"Bootstrap mean estimate: {np.mean(bootstrap_means):.3f}")
    
    # Bootstrap confidence interval for median
    lower_med, upper_med, bootstrap_medians = bootstrap_analyzer.confidence_interval(np.median, confidence_interval)
    # print(f"\n95% Bootstrap Confidence Interval for Median:")
    print(f"Lower bound: {lower_med:.3f}")
    print(f"Upper bound: {upper_med:.3f}")
    print(f"Bootstrap median estimate: {np.mean(bootstrap_medians):.3f}")
    
    # Bias correction
    bias_results = bootstrap_analyzer.bias_correction(np.mean)
    # print(f"\n2. BIAS CORRECTION ANALYSIS")
    print(f"Original estimate: {bias_results['original_estimate']:.3f}")
    print(f"Bootstrap mean: {bias_results['bootstrap_mean']:.3f}")
    print(f"Estimated bias: {bias_results['bias']:.3f}")
    print(f"Bias-corrected estimate: {bias_results['corrected_estimate']:.3f}")
    
    # Visualize initial data and bootstrap results
    print(f"\n2.1. VISUALIZATION")
    print("Creating side-by-side plots of initial data and bootstrap distribution...")
    bootstrap_data = bootstrap_analyzer.get_bootstrap_data(statistic_func=np.mean, confidence_level=confidence_interval)
    BootstrapVisualizer.plot_data_and_bootstrap(bootstrap_data)

    # Bootstrap vs Theoretical Distribution
    print(f"\n2.2. BOOTSTRAP VS THEORETICAL DISTRIBUTION")
    print("Creating comparison plot of bootstrap vs theoretical distribution...")
    BootstrapVisualizer.plot_bootstrap_vs_theoretical(bootstrap_data)

    # Confidence Interval Comparison
    print(f"\n2.3. CONFIDENCE INTERVAL COMPARISON")
    print("Creating confidence interval comparison across different confidence levels...")
    ci_comparison_data = bootstrap_analyzer.get_confidence_interval_comparison_data(
        statistic_func=np.mean,
        confidence_levels=[0.90, 0.95, 0.99]
    )
    BootstrapVisualizer.plot_confidence_interval_comparison(ci_comparison_data)
    
    # Model bootstrap demonstration
    print(f"\n3. MODEL BOOTSTRAP DEMONSTRATION")
    
    # Generate regression data
    X = np.random.randn(sample_size, 2)
    true_coefficients = [3, -2]
    y = X @ true_coefficients + np.random.randn(sample_size) * 0.5
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Model bootstrap
    model_bootstrap = ModelBootstrap(X_train, y_train, LinearRegression, n_bootstrap=sample_size)
    
    # Get prediction intervals
    pred_intervals = model_bootstrap.prediction_intervals(X_test, confidence_level=confidence_interval)
    
    print(f"Test set size: {len(X_test)}")
    print(f"Mean prediction: {np.mean(pred_intervals['mean_prediction']):.3f}")
    print(f"Average prediction interval width: {np.mean(pred_intervals['upper_bound'] - pred_intervals['lower_bound']):.3f}")
    
    # Calculate coverage (how many true values fall within prediction intervals)
    coverage = np.mean((y_test >= pred_intervals['lower_bound']) & 
                      (y_test <= pred_intervals['upper_bound']))
    print(f"Prediction interval coverage: {coverage:.1%}")


if __name__ == "__main__":
    # Run demonstrations
    demonstrate_bootstrapping()
