# dataset-tools

Various tools for working with datasets and creating machine learning models.


# Scripts

## merge 

This tool is used to merge datasets. Usage:

```bash
python -m scripts.merge <source_dataset> <destination_dataset>
```

Where:
  * source_dataset - Path to csv file with information about data which should be merge into destination dataset
  * destination_dataset - Path to csv file where the data should be added.

  
## Retrain model

```bash
ARCHITECTURE="mobilenet_0.50_224"

python -m scripts.retrain --bottleneck_dir=build/bottlenecks --how_many_training_steps=500 --model_dir=build/models/ --summaries_dir=build/training_summaries/"${ARCHITECTURE}" --output_graph=build/retrained_graph.pb --output_labels=build/retrained_labels.txt --architecture="${ARCHITECTURE}" --image_dir=dataset/card-colors
```

## Convert to CoreML model

```bash
python -m scripts.convert build/optimized_graph.pb build/CardColors.mlmodel
```


# Additional tools

## Preview label

```bash
python -m scripts.label_image --graph=build/retrained_graph.pb --labels=build/retrained_labels.txt --image=dataset/card-colors/diamonds/83772cbc-d6c9-4076-a7f8-30e06618ea09.jpg
```

## Optimize model

```bash
python -m tensorflow.python.tools.optimize_for_inference --input=build/retrained_graph.pb --output=build/optimized_graph.pb --input_names="input" --output_names="final_result"
```

## Inspect model

```bash
python -m utils.inspect_pb build/optimized_graph.pb build/info_pb.txt
```



# Contribution

Some files are taken from: https://github.com/googlecodelabs/tensorflow-for-poets-2.
Check this project out, it is worth it.