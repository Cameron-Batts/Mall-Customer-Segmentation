# Mall Customer Segmentation and PCA
**Cameron Batts**

## Validation update - October 22, 2026

All six K-Means/Ward searches selected six clusters. Standardized PCA retained 44.27% of variance with one component and 77.57% with two. All 12 code cells and eight figures were regenerated using the documented replacement helper. Internal cluster metrics do not establish actionable segments or stability.

[Aggregate validation record](Reports/validation_results.json). [Repeatable validation script](validation/rerun_analysis.py). Run `python validation/rerun_analysis.py` from the project root. Install `requirements-validation.txt` first; source CSVs stay local.

## Problem
Compare cluster-count heuristics and examine how much information PCA retains in three customer attributes.

## Approach
Use 200 customers with age, annual income and spending score. Evaluate k=2–14 using K-Means and Ward agglomerative clustering with Calinski–Harabasz, negated Davies–Bouldin and silhouette scores. Clustering uses original feature scales; PCA uses standardized features.

## Historical findings and original context
The original six saved clustering searches all selected six clusters. Standardized PCA retained 44.27% of variance with one component and 77.57% with two. Agreement between internal metrics supports further exploration; it does not prove actionable customer segments.

## Limitations
The original plotting/tuning helper was absent. A replacement is now bundled with explicit random_state=42 and n_init=10; results may differ from the historical outputs. Fresh full-notebook outputs are now saved; the replacement helper remains explicitly distinguished from the absent historical helper. Clustering is sensitive to feature scales, seeds and sample composition. No stability analysis, customer-level segment profiles or campaign validation was performed.

## Data
Data/mall_customers.csv contains 200 records. CustomerID and Gender are excluded from modeling. The original repository did not document a dataset source or license; provenance remains unverified.

## Verification
The full notebook now executes with the replacement helper. See the fresh validation record; helper_validation.txt is an earlier partial check.

## Run
```bash
python -m pip install -r requirements.txt
jupyter lab
```
Open [the notebook](Notebooks/mall_customer_segmentation.ipynb) and run cells in order. Tested numerical/NLP packages are recorded in requirements-validation.txt.

## Files
- [Analysis report](Reports/mall_customer_segmentation.html)
- [Original PDF](Reports/mall_customer_segmentation.pdf): historical export; may predate corrections.
- [Live portfolio report](https://cameron-batts.github.io/mall_customer_segmentation.html)
