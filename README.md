# The Good Alarm Clock

![The Good Alarm Clock picture](https://weareleto.com/wp-content/uploads/2017/01/2017-01-24-10.07.04.jpg)

This repository contains the Flask code for The Good Alarm Clock powered by Raspberry Pi - a [LETO](https://weareleto.com) hackathon project.

[Read the full write-up](http://weareleto.com/experiments/good-alarm-clock/) on what this is all about on our blog.

## Installation

1. Clone the repository `git clone git@github.com:letolab/goodclock.git`
2. Start Vagrant box `vagrant up`
3. SSH into the box `vagrant ssh`
4. Change to the project folder `cd /vagrant`
4. Start the server `python server.py`
5. In your browser, go to `http://localhost:8080`

## Usage

This repo contains the code for the Alarm Clock to run on your Raspberry Pi. You can also find the STL models for 3D printing in `enclosure`

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

Made by LETO in London with ❤ by the team of:

- [Paulo Gonçalves](https://github.com/prpgleto)
- [Matt Duck](https://github.com/mattduck)
- [Alex Berezovskiy](https://github.com/letoosh)

Icons by [Freepik](http://www.freepik.com)

## License

Copyright (c) 2017 LETO

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

