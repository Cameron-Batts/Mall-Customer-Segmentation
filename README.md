# Mall Customer Segmentation and PCA
**Cameron Batts**

## Problem
Compare cluster-count heuristics and examine how much information PCA retains in three customer attributes.

## Approach
Use 200 customers with age, annual income and spending score. Evaluate k=2–14 using K-Means and Ward agglomerative clustering with Calinski–Harabasz, negated Davies–Bouldin and silhouette scores. Clustering uses original feature scales; PCA uses standardized features.

## Results
The original six saved clustering searches all selected six clusters. Standardized PCA retained 44.27% of variance with one component and 77.57% with two. Agreement between internal metrics supports further exploration; it does not prove actionable customer segments.

## Limitations
The original plotting/tuning helper was absent. A replacement is now bundled with explicit random_state=42 and n_init=10; results may differ from the historical outputs. Original clustering outputs are retained and labeled, and the replacement helper is checked separately. Clustering is sensitive to feature scales, seeds and sample composition. No stability analysis, customer-level segment profiles or campaign validation was performed.

## Data
Data/mall_customers.csv contains 200 records. CustomerID and Gender are excluded from modeling. The original repository did not document a dataset source or license; provenance remains unverified.

## Verification
Replacement helper executed successfully for all six searches; historical notebook outputs retained without a full notebook rerun. See helper_validation.txt.

## Run
```bash
python -m pip install -r requirements.txt
jupyter lab
```
Open [the notebook](Notebooks/mall_customer_segmentation.ipynb) and run cells in order. Dependencies are unpinned.

## Files
- [Analysis report](Reports/mall_customer_segmentation.html)
- [Original PDF](Reports/mall_customer_segmentation.pdf): historical export; may predate corrections.
- [Live portfolio report](https://cameron-batts.github.io/mall_customer_segmentation.html)
