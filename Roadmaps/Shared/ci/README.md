# Shared Dagger and GitLab recipe

The Python client recipe runs the same named checks locally and on GitLab. It pins Dagger engine and SDK to **0.21.11**, the stable release observed on 2026-11-02. The upstream documentation currently defaults to 1.0 beta; do not mix those module formats into this pinned client recipe. Sources: [stable release](https://github.com/dagger/dagger/releases/tag/v0.21.11), [Python SDK](https://docs.dagger.io/reference/sdks/python/).

Provision an accepted runner with the pinned CLI/SDK and a qualified Python 3.14 image. Set `AEGIS_CI_PYTHON_IMAGE` to the immutable `name@sha256:...` identity. The recipe fails before execution if those pins are absent or inconsistent. Run `python -B Roadmaps/Shared/ci/runner.py` both locally and from the supplied GitLab include. Do not substitute a floating image tag to bypass qualification.

The include serializes state-changing integration at the runner level using a resource group. That is supplementary to Aegis's cross-project agent/session lease. Evidence artifacts retain the engine/image, exact argv and outputs. A12 must add actual source/tree/package and integrated-remote identity checks for project releases, test deployment rollback, and record successful GitLab execution before claiming CI acceptance.

This package supplies the executable recipe and configuration. Dagger/GitLab execution is not asserted by local Python tests or syntax validation. No pipeline credentials or deployed governance are changed by authoring these files.
