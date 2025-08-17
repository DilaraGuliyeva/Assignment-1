# Assignment
# This is the first big project that you will implement from the scratch.
# Of course first and foremost your program should work correctly. However, as we have discussed many of times
# correctness of program alone does not necessarily mean it is a good software. 
# While our goal is to write a program that works, it is also equally important to not write a crap software.
# As you are brainstorming about your approach (where to start, what to use), think about what are the things that are important for a good software.
# Some examples of these we have talked about are:
# - Good software should be fast.
# - Good software should be clean and easily readable.
# - Good software should be maintainable.
# - Good software should be expandable.

# Even though the goal of the assignment is clearly outlined down below, the task at hand is very open ended. You might feel overwhelmed and these are
# some pieces of advice that we have talked about:
# - Spend a lot of time understanding what is exactly being asked to do.
# - Do not rush to writing code.
# - Plan at the high level first then dive deep into the implementation details.
# - Write your steps/plan/ideas down (human brain has little capacity to keep many things in mind actievely, that is why having things
#   written down in front of you will help).
# - As you are developing your code, develop it incrementally (write a bit of code then test it before going any further).
# - COMMIT YOUR CHANGES OFTEN AND WRITE GOOD COMMIT MESSAGES!!!!!
# - Follow some of the basic but good programming practicies: write type of variables in your methods/functions, put down docstrings in your functions.

# Note that I will evaluate your program as a whole and occasioanlly give feedback and some parts of the program. However, checking every line stops
# being feasible and we start developing bigger projects. Hence, it will be totally up to be able to find the issues in your code when things do not work
# and fixing them. My guess is you will need to use debugger heavily when things go wrong.

# I expext you to create a GitHub repository for this and for each upcoming projects and push your local changes to GitHub often.

# GOOD LUCK!

# Assignment description:
# You are working in a big a corporation that is manifacturing parts for space aircract. The parts that are being manufactured
# are called cartridges. Cartridges follow an industry standard and have EEPROM parts to them. 
# EEPROM is essentially a storage on a device that holds certain data that manufacturer decides to put there.
# The cartridges that your company manufactures has many sub-parts to them as well and for each sub-part, there is an entry in EEPROM.
# Explanation on how entries in EEPROM work are in example-eeprom.log

# To get the data from EEPROM for each subpart you would use a command line tools like so: data -p <subpart_name>
# Note that the above command is not available on your command line.

# Now for each sub-part of the cartriedge the data in EEPROM follows exactly the same format.

# Your company has recently discovered that some of the parts have wrong EEPROM data in them. This is bad as with wrong EEPROM data,
# the cartridges do not work properly and might lead to a crash of an aircraft. Hence, your manager asked you to write a software
# using which you can identify the cartridged with bad EEPROM data in them.

# We are interested in sub-part called "Wheel". Hence, to get the EEPROM data for the "Wheel" subpart, we would run the command: data -p wheel
# Getting the data is already done by your colleague Jessica. Jessica ran the commands on each cartridge and gathered the EEPROM data back for
#  the "Wheel" component and stored them in files. Example file Jessica has is colleague-file.log

# Each cartridge has 4 wheel sub-components in them. Hence, there are 4 seperate entries in EEPROM (1 for each component).
# Hence, on each file that your colleague provides you with there are 4 EEPROM "Wheel" component data in them.

# What you need to do?
# - You need to write a program that takes a file name containing the EEPROM data and decide if all the "Wheel" components for that cartridge have
# the correct data. 
# - Your program should print "Yes" or "No" as well as provide what is wrong with the "Wheel" components' data in the file.
# - Your program needs to check integrity of all the data points by validating the checksum wherever possible.
# - Your program should print each possible mini-component in the datagram for each Wheel component. Each mini-component should be on its own line for clarity.
# -.There should be 4 wheel components named Wheel1, Wheel2, Wheel3, Wheel4 in each file.
# - Manufacturing data (date, city and country) should be exaclty same for all the wheel components.
# - Part IDs should be exactly the same.
# - Slot ids should be continuous 4 numbers for each component.