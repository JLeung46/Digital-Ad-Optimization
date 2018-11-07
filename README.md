# Digital Ad Optimization
------------------------------------

Discovers insights into user behavior to predict whether a user will click a given ad. Data was provided by Avito, Russia's largest general classified website that allows sellers to place ads on their site for a wide array of items. Dataset can be obtained [here](https://www.kaggle.com/c/avito-context-ad-clicks/data). Please go [here](https://jleung46.github.io/) for entire analysis and results.

### Installation & Data Download

* Clone this repo.
* Go into folder using 'cd User_Behavior_Ad_Optimization'.
* Make data folder using 'mkdir data'.
* Go into data directory using 'cd data'.
* Download the database [here](https://www.kaggle.com/c/avito-context-ad-clicks/data).
* Extract the downloaded file.
* Extract the database.sqlite file.

* Go back to 'User_Behavior_Ad_Optimization' directory using 'cd ..'.

### Install requirements 

* Install requirements using 'pip install -r requirements.txt'.
	* Make sure to use Python 2.

### Usage

* Run 'mkdir processed' to create a directory for processed data.
* Run 'python get_sample.py' to get a sample of 1M rows.
	* This creates a file called 'sample1M.csv' in the 'processed folder'
* Run 'python process_data.py' to process data.
	* This will create a file called 'processed_data.csv' in the 'processed folder'.
* Run 'python split_data.py' for train/test sets.
	* This creates a file 'train.csv' and 'test.csv' in the 'processed' folder.
* Run 'python predict.py'
	* This trains the model and outputs the AUC score for the model.

### Future Extensions

* Generate more features.
* Use addtional tables from the database.
* Add more data (Use spark to process all 400 million records). 
* Test different algorithms(Random Forest, Boosted Trees).
* Perform Grid Search to optimize parameters.
