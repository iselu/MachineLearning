package cn.edu.hgd.knn;

/**     
 * 类名称：Test    
 * 类描述：    
 *     
 */
public class KnnMain_1 {

	/**    
	 * 方法作用：  主函数，程序入口
	*/
	public static void main(String[] args) {

		Knn knn = new Knn();
		knn.startClassify(); //开始分类
		double error = knn.getErrorRate();
		double right = knn.getRightRate();
		System.out.println("===========================");
		System.out.println("约会网站配对效果错误率：" + error);
		System.out.println("约会网站配对效果正确率：" + right);

	}

}
