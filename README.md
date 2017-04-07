# SleepWell

The script is designed for scraping hotel prices from Trivago website.

It saves scraping result in easy to read HTML file.

# Additional requirements
## Windows
You have to download latest version of PhantomJS and place it in browsers/windows directory.

You can download it from here: http://phantomjs.org/download.html

## Linux
You have to install latest version of PhantomJS.

Here is an instruction: https://gist.github.com/julionc/7476620

# Usage
```
$ app
Usage: app [OPTION] [ARG]...

Options:
  --location (-l)      Continent / country / region/ city
  --date_from (-df)    For example 2017-10-01
  --date_to (-dt)      For example 2017-12-30
  --stars (-s)         You can set 1,2,3,4,5 (all or some of them, default it is all of them)
  --reviews (-r)       You can set 1,2,3,4,5 (all or some of them, default it is all of them)
  --distance (-d)      Distance from city centre (meters) - use it only if location is a city! It is optional argument.
  --max_price (-mp)    You can set how much You can pay per night. It is optional argument.

Usage Example:
   $ app -l Rome -df 2017-10-01 -dt 2017-12-30 -s 3,4,5 -r 4,5 -d 3500 -mp 100   
   $ app -l Amsterdam -df 2017-10-01 -dt 2017-12-30 -s 4,5 -r 2,3,4,5
```

# Report example
![alt tag](https://i.imgur.com/HAGNMYI.png)

# Thanks
Report template
https://github.com/tidusjar/responsive-html-email-template
