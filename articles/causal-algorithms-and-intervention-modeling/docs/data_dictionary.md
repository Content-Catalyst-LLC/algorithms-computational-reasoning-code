# Data Dictionary

The generated data are synthetic. They model a simplified institutional setting in which several intervention candidates can be compared under explicit assumptions.

| Field | Meaning | Intervention role |
|---|---|---|
| `case_id` | Synthetic unit identifier. | Unit of analysis. |
| `baseline_need` | Starting level of need or risk. | Confounder and outcome driver. |
| `access_barrier` | Structural obstacle to receiving benefit. | Possible intervention target. |
| `service_quality` | Quality of service or implementation. | Possible intervention target. |
| `support_intensity` | Intensity of institutional support. | Treatment/intervention lever. |
| `implementation_cost` | Synthetic resource cost. | Net-benefit and feasibility review. |
| `baseline_outcome` | Modeled outcome before intervention. | Comparison state. |
| `intervention_name` | Candidate policy, treatment, or rule change. | Intervention scenario. |
| `intervention_outcome` | Modeled outcome after intervention. | Potential effect record. |
| `estimated_effect` | Difference from baseline outcome. | Target of estimation. |
| `net_benefit` | Effect minus cost and risk penalties. | Decision-support metric. |
| `feasibility_status` | Review status for implementation. | Governance boundary. |

## Boundary

The dataset is designed to teach intervention modeling. It is not calibrated to real populations, policies, or institutional systems.
