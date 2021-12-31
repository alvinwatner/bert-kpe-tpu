export DATA_PATH=../data

# preprocess openkp or kp20k
python3 debug_preprocess.py --dataset_class squadkp \
--source_dataset_dir $DATA_PATH/dataset \
--output_path $DATA_PATH/prepro_dataset \
