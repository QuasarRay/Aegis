# Original Candle authority

`authority.json` pins upstream Git commits and byte hashes of initial specification
anchors. These are references, not copies translated into another specification language.
The full pinned CakeML revision remains the import authority; the anchor list is not a
claim of full formalisation coverage. Use HOL4 to interpret original theories.

Paper: [Candle: A Verified Implementation of HOL Light](https://doi.org/10.4230/LIPIcs.ITP.2022.3),
Abrahamsson, Myreen, Kumar and Sewell, ITP 2022. Scientific disagreements block affected
acceptance until documented and resolved. The paper's soundness theorem must not be
reported as a proof of Rust code, of arbitrary stdout, or of all observable equivalence.

Initial target inspection found only AGENTS.MD and LICENSE.MD at the pinned Candle-rs
revision. No Rust kernel, complete import adapter, or Rust proof is assumed to exist.
