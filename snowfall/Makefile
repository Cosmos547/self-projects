CXX = g++

SDL_LIB = -L/usr/local/lib -lSDL2
SDL_INCLUDE = -I/usr/local/include

CXXFLAGS = -Wall -c -std=c++11 $(STD_INCLUDE)
LDFLAGS = $(SDL_LIB)
EXE = snowfall

all: $(EXE)

$(EXE): main.o
	$(CXX) $< $(LDFLAGS) -o $@

main.o: main.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm *.o && rm $(EXE)
