# "Revert, Revert" Exercise

## Instructions

Navigate to your local fork of the course repository. You should be able to view the history of the commits:

```sh
git log
```

Choose a version you'd like to "roll-back" to and locate its identifier, or "SHA" (e.g. `28a7b0c7281264dd5e519a9a18a9acdb2bb849d9`). Then revert to that version:

```sh
git reset --hard 28a7b0c7281264dd5e519a9a18a9acdb2bb849d9
```

Verify these changes by re-inspecting the version history:

```sh
git log
```

Nice! Afterwards, you may want to [refresh your fork](/CONTRIBUTING.md#refreshing-your-fork) to return it to its most recent state.
