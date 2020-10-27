package queueWithTwoStacks;

import java.util.Stack;

/** Implement Queue (a datastructure with two methods, enqueue() and dequeue()) 
* 	by using two Stacks (java.util.Stack)
*/
public class QueueWithTwoStacks {
	
	Stack<String> in;
	Stack<String> out;
	
	public QueueWithTwoStacks(){
		in = new Stack<String>();
		out = new Stack<String>();
	}
	
	//todo make generic
	public void enqueue(String s){
		in.push(s);
	}
	
	public String dequeue(){
		if(out.empty()){
			while(!in.empty()){
				out.push(in.pop());
			}
		}
		return out.pop();
	}
}