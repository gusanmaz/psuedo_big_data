# Pseudo Big Data Generator

This project aims to ease generation of certain kinds of pseudo data. 

## Motivation

The motivation behind this program is to generate mock-up data to be used in a Data Structures and Algorithms class, in which the author is a co-teacher. The author believes that assigning assignments that encourage students to test their algorithms with larger, more complex and realistic mock-up data would have a positive outcome. In Data Structures and Algorithms classes, students often test complicated algorithms with small data, making it difficult for them to realize the real-world benefits of more complex algorithms with smaller time and space complexity. Furthermore, working with plain data may not be as meaningful to students as working with data that is closer to real-world scenarios. For example, sorting a bunch of numbers may be less relevant compared to sorting bank account data based on their balance.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/username/project.git
```


2. Navigate to the project directory:

```bash
cd project
``` 

3. Create and activate a new virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Run the main script:

```bash
python main.py
```

In the main function, you will find calls to functions that generate mock-up data. These functions have default values for their parameters, which can be modified to suit your needs. If you want to change the default behavior of these function calls, you can modify their parameters accordingly.
## Examples of Pseudo Data for Different Data Types

For now, you can generate data similar to following pseudo data:

* Tabular Data

   * University Student Data `tabular/student.py`

Name         |  Surname      |  Student ID  |  GPA   |  Department                              |  Enrollment Year  |  Date of Birth
-------------|---------------|--------------|--------|------------------------------------------|-------------------|---------------
Kimberly     |  Glass        |  2194452203  |  1.28  |  Environmental Engineering               |  2022             |  1954-06-26
Margaret     |  Dillon       |  2518248525  |  1.63  |  Mechanical Engineering                  |  2016             |  2004-11-12
Megan        |  Jackson      |  1064912807  |  2.54  |  Psychology                              |  2012             |  1962-04-21
Maria        |  Wiggins      |  2138736257  |  3.4   |  Sociology                               |  2021             |  1964-06-07
Robin        |  Barrera      |  2787155251  |  2.16  |  Tourism                                 |  2020             |  1957-10-20
Jessica      |  Thompson     |  2450628649  |  2.47  |  Psychology                              |  2021             |  1973-03-13

  * Bank Account Data `tabular/bank.py` 

Customer ID                           |  SSN Number   |  Customer Name  |  Customer Surname  |  Email                             |  Address Street                       |  Address State   |  Address City              |  Address Country  |  Address Zipcode  |  Phone Number            |  Account Type  |  Account Balance  |  Customer Age  |  Date of Account Opening  |  Customer Gender  |  Customer Occupation                                          |  Customer Education Level
--------------------------------------|---------------|-----------------|--------------------|------------------------------------|---------------------------------------|------------------|----------------------------|-------------------|-------------------|--------------------------|----------------|-------------------|----------------|---------------------------|-------------------|---------------------------------------------------------------|--------------------------
7e245be4-f6e4-4359-a431-f01cd2c24156  |  317-40-7798  |  Connie         |  Williams          |  mitchellgolden@example.net        |  02380 Miguel Square                  |  Massachusetts   |  Gatesberg                 |  USA              |  81082            |  +1-281-370-1004x261     |  Euro          |  78344.42         |  45            |  2002-12-04               |  Female           |  Drilling engineer                                            |  PhD
22dd6103-74a5-4bc0-8ac4-8b48be17befa  |  032-73-1963  |  Brian          |  Sandoval          |  mthompson@example.net             |  9743 Jennifer Grove                  |  Alaska          |  Porterport                |  USA              |  12222            |  +1-326-554-5687         |  TL            |  77012.4          |  32            |  2000-06-02               |  Male             |  Mining engineer                                              |  PhD
ead46a32-1230-410c-8602-b4f1aa7119be  |  252-73-4109  |  Richard        |  Larsen            |  johnroberts@example.com           |  8915 Willis Stravenue                |  Colorado        |  West Matthew              |  USA              |  45542            |  +1-959-994-5360x97310   |  Dollar        |  87172.63         |  75            |  2007-10-01               |  Female           |  Archaeologist                                                |  PhD
5dc232a6-847e-4d96-b197-f254dae9c41a  |  138-49-1931  |  Jason          |  Welch             |  dennispierce@example.com          |  56381 Fox Hills                      |  Florida         |  Davidville                |  USA              |  58107            |  269-514-3995            |  TL            |  95361.65         |  73            |  2013-06-30               |  Male             |  Volunteer coordinator                                        |  Bachelor
3c4fa81d-53ae-47d4-bee5-5dfd62d66670  |  451-72-7652  |  Joseph         |  Barrera           |  david19@example.net               |  99215 Ross Roads                     |  North Carolina  |  Wallside                  |  USA              |  66723            |  997-884-2464            |  Euro          |  20685.92         |  63            |  2003-09-11               |  Female           |  Lobbyist                                                     |  High School
abd33426-8267-40e5-a504-39cfb6dc0a89  |  808-55-2605  |  Joseph         |  Long              |  daniel38@example.net              |  469 Jason Fall                       |  North Dakota    |  Patrickville              |  USA              |  96204            |  +1-161-482-2051x714     |  Euro          |  54050.17         |  46            |  2005-11-10               |  Male             |  Intelligence analyst                                         |  Bachelor
f421be78-9c39-4b5d-97b7-6e37a2f490ef  |  403-43-7916  |  Paula          |  Conner            |  clarkerin@example.com             |  6029 Rose Ways                       |  Nebraska        |  North Davidside           |  USA              |  55425            |  394.422.3793x317        |  TL            |  85434.34         |  27            |  2017-02-08               |  Male             |  Meteorologist                                                |  Bachelor

  * EarthQuake Data `tabular/earthquake.py`

Date        |  City            |  Magnitude  |  Depth (km)  |  Duration (s)  |  Latitude  |  Longitude
------------|------------------|-------------|--------------|----------------|------------|-----------
2015-10-20  |  Bayburt         |  5.6        |  10          |  3.7           |  38.76     |  36.99
2019-08-01  |  Zonguldak       |  4.4        |  65          |  18.1          |  41.45     |  39.54
2019-11-24  |  Manisa          |  6.8        |  5           |  3.3           |  38.07     |  34.15
2022-04-18  |  Eskişehir       |  6.6        |  15          |  4.2           |  40.14     |  28.05
2014-10-22  |  Tokat           |  3.2        |  45          |  9.9           |  40.42     |  35.79
2023-03-14  |  Kastamonu       |  7.0        |  45          |  3.7           |  37.38     |  35.02
2015-09-04  |  Nevşehir        |  4.6        |  5           |  10.2          |  40.42     |  40.51


* Graph Data `graph/train_routes.py`

   * Train Routes Data

Source              |  Destination         |  Distance
--------------------|----------------------|----------
New Jeffreyborough  |  Rodriguezville      |  94
New Jeffreyborough  |  South Donnahaven    |  19
New April           |  Rodriguezville      |  99
Cherylfurt          |  South Donnahaven    |  68
New Wandachester    |  South Donnahaven    |  64
New Jeffreyborough  |  West Kimberly       |  38
Ayersmouth          |  Cherylfurt          |  103
New April           |  New Wandachester    |  146
New Wandachester    |  West Kimberly       |  24
Ayersmouth          |  New April           |  81
Ayersmouth          |  Rodriguezville      |  60
Brianfort           |  New Wandachester    |  62
New Jeffreyborough  |  New Wandachester    |  80
Cherylfurt          |  New April           |  29
Ayersmouth          |  South Donnahaven    |  50
Ayersmouth          |  New Wandachester    |  28
Cherylfurt          |  New Jeffreyborough  |  103
Brianfort           |  South Donnahaven    |  56
Ayersmouth          |  Brianfort           |  23
New Catherine       |  New Wandachester    |  71
New Catherine       |  Rodriguezville      |  90
Rodriguezville      |  South Donnahaven    |  90
New April           |  West Kimberly       |  66
Brianfort           |  New April           |  53
New April           |  New Catherine       |  147
Brianfort           |  West Kimberly       |  69
Brianfort           |  Cherylfurt          |  26

  
  * Social Media Data `graph/social_media.py`

Handle           |  Name      |  Surname    |  Age  |  Email                        |  Total Post Count  |  Following
-----------------|------------|-------------|-------|-------------------------------|--------------------|-----------
mitchellkaitlyn  |  Chelsea   |  Estrada    |  21   |  brenda62@example.com         |  254               |  5
mitchellkaitlyn  |  Chelsea   |  Estrada    |  21   |  brenda62@example.com         |  254               |  4
mitchellkaitlyn  |  Chelsea   |  Estrada    |  21   |  brenda62@example.com         |  254               |  3
mitchellkaitlyn  |  Chelsea   |  Estrada    |  21   |  brenda62@example.com         |  254               |  6
mitchellkaitlyn  |  Chelsea   |  Estrada    |  21   |  brenda62@example.com         |  254               |  9
lynn87           |  Jennifer  |  Wiggins    |  53   |  nelsonjennifer@example.com   |  998               |  6
lynn87           |  Jennifer  |  Wiggins    |  53   |  nelsonjennifer@example.com   |  998               |  1
lynn87           |  Jennifer  |  Wiggins    |  53   |  nelsonjennifer@example.com   |  998               |  2
lynn87           |  Jennifer  |  Wiggins    |  53   |  nelsonjennifer@example.com   |  998               |  5
mark20           |  Patricia  |  Lewis      |  32   |  conniehernandez@example.com  |  144               |  0
mark20           |  Patricia  |  Lewis      |  32   |  conniehernandez@example.com  |  144               |  3
mark20           |  Patricia  |  Lewis      |  32   |  conniehernandez@example.com  |  144               |  1
mark20           |  Patricia  |  Lewis      |  32   |  conniehernandez@example.com  |  144               |  2
mark20           |  Patricia  |  Lewis      |  32   |  conniehernandez@example.com  |  144               |  5
colebrandy       |  Kayla     |  Vargas     |  39   |  brett70@example.com          |  676               |  7
colebrandy       |  Kayla     |  Vargas     |  39   |  brett70@example.com          |  676               |  5
vpatel           |  Tracy     |  Castaneda  |  45   |  weberchristina@example.com   |  393               |  4
vpatel           |  Tracy     |  Castaneda  |  45   |  weberchristina@example.com   |  393               |  9
vpatel           |  Tracy     |  Castaneda  |  45   |  weberchristina@example.com   |  393               |  1
vpatel           |  Tracy     |  Castaneda  |  45   |  weberchristina@example.com   |  393               |  5
ruth11           |  Shannon   |  Smith      |  69   |  timothygarza@example.com     |  466               |  9
ruth11           |  Shannon   |  Smith      |  69   |  timothygarza@example.com     |  466               |  7
frederickdeleon  |  Joshua    |  Johnson    |  38   |  monique65@example.com        |  21                |  2
frederickdeleon  |  Joshua    |  Johnson    |  38   |  monique65@example.com        |  21                |  8
frederickdeleon  |  Joshua    |  Johnson    |  38   |  monique65@example.com        |  21                |  7
walkersandra     |  Amber     |  Brown      |  77   |  heathersmith@example.com     |  937               |  6


## Contribution

We welcome contributions to this project! If you're interested in contributing, please follow these steps:

1. Fork the project repository.
2. Create a new branch for your changes. 
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository.

Additionally, if you have an idea for a new kind of mock-up data that needs to be generated by a function, feel free to start a discussion on our Github discussion page. If you encounter any issues or bugs, please report them on our Issues page. We appreciate your contributions!

## License:

The code in this project is licensed under the MIT License

## Author:

This project was created by Güvenç USANMAZ. If you have any questions, comments or suggestions, you can contact me me through the project's GitHub page.