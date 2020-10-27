package queueWithTwoStacks;

import java.util.Stack;

/** Implement Queue (a datastructure with two methods, enqueue() and dequeue()) 
* 	by using two Stacks (java.util.Stack)
*/
public class QueueWithTwoStacksTest {
	
	public static void main(String[] args)
	{
		System.out.println("Testing...");
		test();
		System.out.println("OK");
	}
	
	public static void test(){
		QueueWithTwoStacks q = new QueueWithTwoStacks();
		q.enqueue("s1");
		verify(q.dequeue(), "s1");
		q.enqueue("s2");
		q.enqueue("s3");
		verify(q.dequeue(), "s2");
		q.enqueue("s4");
		verify(q.dequeue(), "s3");
		verify(q.dequeue(), "s4");
	}
	
	public static void verify(Object actual, Object expected){
		if(!expected.equals(actual)){
			throw new AssertionError("expected '" + expected.toString() + "' but was '" + actual.toString() + "'");
		}
	}
	
}