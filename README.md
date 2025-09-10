# Predicting Vote Share Based on Cook PVI

The Cook PVI is a measure of how much more Republican or Democrat your state/district is compared to the national environment. For exmaple, a PVI of R+5 would mean a state/district is
5 percentage points more Republican than the nation, and a PVI of D+5 would mean a state/district is 5 percentage points more Democrat than the nation. For the purposes of this program,
Republican PVI's are represented as positive numbers and Democrat PVI's are represented as negative numbers.

Depending on a states'/districts' PVI, the vote share for a Republican or Democrat either increases or decreases. Naturally, a more Republican PVI would mean the Republican gets more
votes, and vice versa for the Democrat with a more Democrat PVI. Based on this, I created two separate one variable linear regression models to predict the vote share for a Republican
or Democrat based on an entered PVI.

The data that the models were trained on include 2020 and 2024 presidential election results, and 2022 and 2024 US Senate election results. The data, which includes
a states' 2025 Cook PVI and the vote share of the Republican and Democrat are stored in two csv files, separated by party.

The purpose of this project is to start learning about machine learning and how to implement different models for it. The topic of Cook PVI and Vote Share was picked due to my interest
in political technology.

## Getting Started

These instructions will show you how to get a copy of the project and run it on your computer

### Prerequisites

* Python installed on your computer

### Installation

Open up the terminal in the project directory

If using python 3 or higher, run

```
$ pip3 install numpy
```

Otherwise run

```
$ pip install numpy
```

## Usage

Run the program in your desired development environment

The program will ask for an input, either a positive or negative number representing the PVI

The following is an example after running the program stored in 'r_linear_regression.py'

```
$ Please enter a Cook PVI value (negatives represent more Democrat, positives represent more Republican)
$ 0
$ Based on a Cook PVI of [0], a Republican is expected to get 48.53% of the vote
```
The following is an example after running the program stored in 'd_linear_regression.py'

```
$ Please enter a Cook PVI value (negatives represent more Democrat, positives represent more Republican)
$ 0
$ Based on a Cook PVI of [0], a Democrat is expected to get 49.65% of the vote
```
