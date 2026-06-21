# Governance Checklist

- Was the test set protected from model selection and tuning?
- Were validation choices documented before final testing?
- Is there a visible generalization gap between training and held-out data?
- Does performance change under shifted conditions?
- Are subgroup metrics reported when performance may be uneven?
- Are probability scores calibrated enough for the intended use?
- Are benchmark results being overstated as proof of deployment reliability?
- Is the use boundary documented for contexts outside the evaluated data?
