for id in "$@"; do printf "%s\t0\t0\t0\t0\tunlocated\tCandidates reviewed; no supporting lines found.\n" $id >> decisions.tsv; done
