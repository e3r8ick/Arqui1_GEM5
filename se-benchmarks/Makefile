SRCS = $(wildcard *.c)
PROGS = $(patsubst %.c,%,$(SRCS))
all: $(PROGS)
%: %.c
	arm-linux-gnueabihf-gcc --static $< -o $@
clean:
	rm -f $(PROGS)