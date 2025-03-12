import kaggle

dataset_slug = "clmentbisaillon/fake-and-real-news-dataset"

kaggle.api.dataset_download_files(dataset_slug, unzip=True)