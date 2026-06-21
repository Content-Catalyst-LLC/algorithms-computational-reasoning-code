type Contrast = {
  treatedMean: number;
  controlMean: number;
};

function effect(contrast: Contrast): number {
  return contrast.treatedMean - contrast.controlMean;
}

console.log(`causal contrast = ${effect({ treatedMean: 0.64, controlMean: 0.47 }).toFixed(4)}`);
