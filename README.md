
# Jolygones
A short Python implementation of "Jolygones", an idea I read about in the french magazine "Tangente".

## Getting started

These instructions will let you run the code and generate as many Jolygones as you'd like.

### Prerequisites

Installed on your computer :
```
Python3
```
As well as a way to display svg graphics (a web browser or most image viewers will work).

## Running the code

The syntax is the following :
```
./jolygones -a <angle> -i <iterations> -c <coefficient> -s <size>
```

* angle is in degrees and should be less or equal to 90 degrees if you want the figure to loop inwards.
* iterations is the number of segments that will be displayed.
* coeeficient dictates how the segments grow or shrink. It should be less than one if you want the figure to shrink.
* size is the size of the first segment in pixels.

The image generated will be called "test.svg".

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Jules Simon** - *Initial work* - [Smoltbob](https://github.com/Smoltbob)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Tangente magazine](http://tangente-mag.com/) 
