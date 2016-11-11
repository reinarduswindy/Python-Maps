#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

class Test {
public:
	std::string test() {
		return "Hello, World!";
	}

	char* hello(char* name)
	{ 
	    char hello[] = "Hello, ";
	    char excla[] = "!";
	    char *greeting = new char[sizeof(char) * ( strlen(name) + strlen(hello) + strlen(excla) + 1 )];
	    // char *greeting = malloc ( sizeof(char) * ( strlen(name) + strlen(hello) + strlen(excla) + 1 ) );
	    if( greeting == NULL) exit(1);
	    strcpy( greeting , hello);
	    strcat(greeting, name);
	    strcat(greeting, excla);
	    return greeting;
	}
};

extern "C" {
	Test* test_new() {
		return new Test();
	}
	std::string test_print(Test* test) {
		return test->test();
	}
	char* test_hello(Test* test, char* name) {
		return test->hello(name);
	}
}