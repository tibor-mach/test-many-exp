for ((i = 0 ; i < 100 ; i++)); do
	dvc exp run --queue -S x=$i
done

dvc exp run --run-all -j 20