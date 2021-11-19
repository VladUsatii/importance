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

First, place the importance directory in your project folder. Should be relative to the files. Then, run an init:

```bash
>>> cd [ project_name ]
>>> importance gen
```

To config a colored directory:

```bash
>>> cd importance
>>> vi active.txt # if active project
>>> vi important.txt # if important project
>>> # updateable will autoconfig soon
```
