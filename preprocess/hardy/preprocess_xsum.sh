export DATA_PATH=/home/acp16hh/Projects/Research/Data/Summarization/ready
export OUTPUT_PATH=/home/acp16hh/Projects/Research/Data/Summarization/for_model/xsum/jointkpe
export CUDA_VISIBLE_DEVICES=0

# preprocess openkp or kp20k
python preprocess.py --dataset_class xsum \
--source_dataset_dir $DATA_PATH \
--output_path $OUTPUT_PATH/prepro_dataset \
