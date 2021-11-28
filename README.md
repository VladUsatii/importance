# importance ⚠️

A virtual terminal ```ls``` that color-codes projects by importance.

| Color	      | Description		|
| ----------- | ---------------	|
| Red	      | Super important	|
| Green       | Active			|
| Yellow	  | Updateable		|
| White		  | Not important	|

### Example 🎨

Here is an example of a color-coded folder. It is super important.

![Here is an example of an important tab](https://github.com/VladUsatii/importance/blob/main/demo.png?raw=true)


### Config ⚙️

To get importance in your directory, ```cd``` into it and clone importance relative to it:

```bash
>>> cd [ project_name ]
>>> git clone "https://github.com/VladUsatii/importance.git"
>>> cd importance
>>> bash setup.sh # first time user only
```

To test it, type ```cls```. **We are aware that ```cls``` is also used for ```clear``` on some systems.**:

```bash
>>> cls
```

To add a file as important (red) or active (green):

```bash
>>> cls-red [ filename ]
>>> cls-green [ filename ]
```

Enjoy 😊

---

### Popular Questions

**Isn't ```cls``` the clear screen command?**

It is the clear screen command, but keep in mind that this utility was designed for Unix/MacOS primarily. I might port this to other OSes in the future, but I see no point as this is where I do a lot of my work.

**Is this a package?**

This will never be a package. I find it much more handy to git clone the importance repository in all of my projects where I need to color-code files by importance. This eliminates the confusion from appending via the ```cls-red``` and ```cls-green``` commands.

---

Created by Vlad Usatii @ youshould.readproduct.com
