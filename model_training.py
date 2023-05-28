from fastbook import *
from fastai.vision.widgets import *

## Gathering Data

path = Path('data_devices')

device_types = 'laptop','desktop pc','mobile phone'

if not path.exists():
    path.mkdir()
    for o in device_types:
        dest = (path/o)
        dest.mkdir(exist_ok=True)
        results = search_images_ddg(f'{o}', max_images=100)
        # results = search_images_bing(key, f'{o} bear')
        # download_images(dest, urls=results.attrgot('contentUrl'))
        download_images(dest, urls=results)
fns = get_image_files(path)


failed = verify_images(fns)


failed.map(Path.unlink);

#* 
## From Data to DataLoaders
devices = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128))
dls = devices.dataloaders(path)





### Data Augmentation


## Training Your Model, and Using It to Clean Your Data
devices = devices.new(
    item_tfms=RandomResizedCrop(224, min_scale=0.5),
    batch_tfms=aug_transforms())
dls = devices.dataloaders(path)
learn = vision_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(4)
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()




## Turning Your Model into an Online Application

### Using the Model for Inference
learn.export()
path = Path()
path.ls(file_exts='.pkl')
learn_inf = load_learner(path/'export.pkl')
query02 = "dell inspiron"
urls = search_images_ddg(query02, max_images = 5 )
dest = f'data_test/{query02}.jpg'
download_url(urls[0], dest)
learn_inf.predict(dest)

