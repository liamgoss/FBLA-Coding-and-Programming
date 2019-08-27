**Welcome** Upon startup, the user will be greeted with the Check Out
Screen which has the following features: Student Information Class Roll
Sheet (see '**Importing Data**') A calendar which is automatically set
to the current day A blank table with a 'Confirm' button (see
'**Checking Out Items**') The other tabs are 'Return' and 'Library'. The
'Return' tab is identical to the 'Check Out' tab in appearance. The
'Library' tab contains the following: A calendar, identical to those
found in other tabs An empty Library Table (see '**Importing Data**') 2
buttons (see '**Switching Gears**')

**Importing Data** Before the program can function properly, the user
must direct the program to the class 'Roll Sheet' and 'Library' CSV
files. To do so, go to File \> Import Roll Sheet, then navigate to the
'src' directory and select 'Roll Sheet.csv'. Upon completion, the Class
Roll Sheet tables in the 'Check Out' and 'Return' tabs will be updated
with a list of students and other important information such as
students' grade levels and ID numbers. Now that the roll sheet is up to
date, the user must load the list of e-books available by following the
same steps as before: go to File \> Import Library and select
'Library.csv' in the 'src' folder.

\*Note, to locate the 'src' folder, the user may need to go back one or
more directories

Now that all of the necessary information is loaded in, the user is
ready for the '**Checking Out Items**' section.

**Checking Out Items** Checking out items is simple and easy, just go to
the 'Check Out' tab to begin! In the lower left hand corner, a list of
students is displayed and to select one, just double click their name or
ID number. If done correctly, the student's information will be
displayed in the upper left hand corner of the window. To add items to
the student's account, simply go to the 'Library' tab and double click
up to 5 e-books The confirm button will create a flattened file to be
loaded in later (see '**Advanced Features**')

**Switching Gears** To return an item, simply navigate to the 'Library'
tab and check the 'Return' option Then move on to **Returning Items**

**Return Items** Now that the 'Return' option is checked, simply select
the objects to return from the Library and press confirm!

**Advanced Features** The confirmation buttons create flattened files,
as described above, in temporary directories and are deleted upon the
close of the application. In order to save this file ('dict.pickle'),
navigate to the appropriate tmp directory and save a copy. An AES
encrypted file ('dict.pickle.aes') will be stored in the current working
directory.
