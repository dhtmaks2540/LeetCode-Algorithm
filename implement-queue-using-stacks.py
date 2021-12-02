class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        # peek를 통해 self.input -> self.output(순서 변경)
        self.peek()
        return self.output.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        
        return self.output[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.input == [] and self.output == []