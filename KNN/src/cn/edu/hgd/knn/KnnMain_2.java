package cn.edu.hgd.knn;

import java.util.Scanner;

/**     
 * 类名称：KnnMain_2    
 * 类描述：     输入一个人，判断其所属分类
 *     
 */
public class KnnMain_2 {

	/**    
	 * 方法作用：  
	 * @return      
	*/
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double f;
		double g;
		double ice;
		System.out.println("请输入该人每年的飞行上的里程数(>0):");
		f = sc.nextDouble();
		System.out.println("请输入该人玩游戏视频所耗时间百分比(0-100):");
		g = sc.nextDouble();
		System.out.println("请输入该人每周消费的冰淇淋公升数量(>=0):");
		ice = sc.nextDouble();

		Knn knn = new Knn();
		People people = new People(f, g, ice);
		knn.judgeInputPersonType(people);

	}

}
