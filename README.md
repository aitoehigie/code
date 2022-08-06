# Getting Started with Weaviate

Weaviate_tutorial is the accompanying source code to the Getting Started with Weaviate tutorial.

## Installation

Unpack the archive into a directory, change into the directory and run this command:

```bash
python setup.py install
```

## Usage

```bash
$ weaviate_tutorial menu

*******************************************************************************
💥 🥳 Welcome to the Getting Started with 💻 Weaviate Tutorial 📖  💥
*******************************************************************************
Enter the following commands in the displayed order to set up the test database and and to be able to query it
-------------------------------------------------------------------------------
Setup database
Enter '1': To generate test data
Enter '2': To upload the schema
Enter '3': To import a single data record
Enter '4': To import bulk test data records
*******************************************************************************
Tutorial
Enter '5': To list all authors
Enter '6': To list all blog posts
Enter '7': To search for authors
Enter '8': To search for blog posts
Enter 0: To exit the application
*******************************************************************************
Enter your choice: 1
Status: Generating data...
Generating data records... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Generated 10000 records.
Status: Generated data successfully!
-------------------------------------------------------------------------------
Enter your choice: 2
File name [data/schema.json]:
Status:Uploading schema...
Status: Schema uploaded!
-------------------------------------------------------------------------------
Enter your choice: 3
Status: importing a single record...
Status: Single record imported successfully!
-------------------------------------------------------------------------------
Enter your choice: 4
Batch importing data...
Data imported!
-------------------------------------------------------------------------------
Enter your choice: 5
{
  "data": {
    "Get": {
      "Author": [
        {
          "name": "Karen Madden",
          "wrotePosts": [
            {
              "body": "Whose class improve large option class. Door throughout stop charge Mr. Not forward nation from. Finally teacher after culture. Start up sing prepare himself impact themselves always. Concern wonder price pay treat. Region apply later training parent. Include lawyer light reach space. Card kind best down partner research if. Much general whole agreement. Evidence leader born road might. Decade remain memory family anything. Range another protect me. Different employee degree man world foot. Despite bring vote want quite economy per enough. Tend party soon perform official. They daughter clearly start foot huge. Forward probably discuss nor. Picture lay actually best study remain husband. Wall medical reach save national learn raise. Employee including stuff phone rate. About exist policy choice husband event name. Size purpose necessary thousand in tax. Which officer number may us. Billion occur media last. Response poor major find large life. Until age her coach candidate. Recent suffer new realize market around Congress sell. Clear see case growth cost none. Your garden month wide off inside. Mother movement nothing behind marriage theory campaign. Well film should. More dream not heart watch own water. Fight even fine southern study. Religious age can. Tend member beat question popular hour. State military might threat charge. Arm grow certain word society. Work fly would certainly property challenge. Leader capital best picture. Yes way house everybody. Around ask sister blue official. Threat down it democratic tough worry how. Threat agent close deep compare generation arrive.",
              "title": "Again then fact whole commercial author hotel."
            }
          ]
        }
      ]
    }
  }
}
-------------------------------------------------------------------------------
Enter your choice: 6
{
  "data": {
    "Get": {
      "BlogPost": [
        {
          "authoredBy": [
            {
              "name": "Karen Madden"
            }
          ],
          "body": "Whose class improve large option class. Door throughout stop charge Mr. Not forward nation from. Finally teacher after culture. Start up sing prepare himself impact themselves always. Concern wonder price pay treat. Region apply later training parent. Include lawyer light reach space. Card kind best down partner research if. Much general whole agreement. Evidence leader born road might. Decade remain memory family anything. Range another protect me. Different employee degree man world foot. Despite bring vote want quite economy per enough. Tend party soon perform official. They daughter clearly start foot huge. Forward probably discuss nor. Picture lay actually best study remain husband. Wall medical reach save national learn raise. Employee including stuff phone rate. About exist policy choice husband event name. Size purpose necessary thousand in tax. Which officer number may us. Billion occur media last. Response poor major find large life. Until age her coach candidate. Recent suffer new realize market around Congress sell. Clear see case growth cost none. Your garden month wide off inside. Mother movement nothing behind marriage theory campaign. Well film should. More dream not heart watch own water. Fight even fine southern study. Religious age can. Tend member beat question popular hour. State military might threat charge. Arm grow certain word society. Work fly would certainly property challenge. Leader capital best picture. Yes way house everybody. Around ask sister blue official. Threat down it democratic tough worry how. Threat agent close deep compare generation arrive.",
          "title": "Again then fact whole commercial author hotel."
        }
      ]
    }
  }
}
-------------------------------------------------------------------------------
Enter your choice: 7
Enter the author's name: Karen
Status: Searching for 'Karen' in authors
{
  "data": {
    "Get": {
      "Author": [
        {
          "name": "Karen Madden",
          "wrotePosts": [
            {
              "body": "Whose class improve large option class. Door throughout stop charge Mr. Not forward nation from. Finally teacher after culture. Start up sing prepare himself impact themselves always. Concern wonder price pay treat. Region apply later training parent. Include lawyer light reach space. Card kind best down partner research if. Much general whole agreement. Evidence leader born road might. Decade remain memory family anything. Range another protect me. Different employee degree man world foot. Despite bring vote want quite economy per enough. Tend party soon perform official. They daughter clearly start foot huge. Forward probably discuss nor. Picture lay actually best study remain husband. Wall medical reach save national learn raise. Employee including stuff phone rate. About exist policy choice husband event name. Size purpose necessary thousand in tax. Which officer number may us. Billion occur media last. Response poor major find large life. Until age her coach candidate. Recent suffer new realize market around Congress sell. Clear see case growth cost none. Your garden month wide off inside. Mother movement nothing behind marriage theory campaign. Well film should. More dream not heart watch own water. Fight even fine southern study. Religious age can. Tend member beat question popular hour. State military might threat charge. Arm grow certain word society. Work fly would certainly property challenge. Leader capital best picture. Yes way house everybody. Around ask sister blue official. Threat down it democratic tough worry how. Threat agent close deep compare generation arrive.",
              "title": "Again then fact whole commercial author hotel."
            }
          ]
        }
      ]
    }
  }
}
-------------------------------------------------------------------------------
Enter your choice: 8
Enter the blog post search term: : Religious age can
Status: Searching for 'Religious age can' in blog posts
{
  "data": {
    "Get": {
      "BlogPost": [
        {
          "authoredBy": [
            {
              "name": "Karen Madden"
            }
          ],
          "body": "Whose class improve large option class. Door throughout stop charge Mr. Not forward nation from. Finally teacher after culture. Start up sing prepare himself impact themselves always. Concern wonder price pay treat. Region apply later training parent. Include lawyer light reach space. Card kind best down partner research if. Much general whole agreement. Evidence leader born road might. Decade remain memory family anything. Range another protect me. Different employee degree man world foot. Despite bring vote want quite economy per enough. Tend party soon perform official. They daughter clearly start foot huge. Forward probably discuss nor. Picture lay actually best study remain husband. Wall medical reach save national learn raise. Employee including stuff phone rate. About exist policy choice husband event name. Size purpose necessary thousand in tax. Which officer number may us. Billion occur media last. Response poor major find large life. Until age her coach candidate. Recent suffer new realize market around Congress sell. Clear see case growth cost none. Your garden month wide off inside. Mother movement nothing behind marriage theory campaign. Well film should. More dream not heart watch own water. Fight even fine southern study. Religious age can. Tend member beat question popular hour. State military might threat charge. Arm grow certain word society. Work fly would certainly property challenge. Leader capital best picture. Yes way house everybody. Around ask sister blue official. Threat down it democratic tough worry how. Threat agent close deep compare generation arrive.",
          "title": "Again then fact whole commercial author hotel."
        }
      ]
    }
  }
}

-------------------------------------------------------------------------------
Enter your choice: 0
Exiting the program now!

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
