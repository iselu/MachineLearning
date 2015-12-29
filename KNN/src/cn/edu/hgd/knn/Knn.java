package cn.edu.hgd.knn;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;

/**     
 * 类名称：Knn    
 * 类描述：    k近邻算法的类
 *     
 */
public class Knn {
	private static int k = 10; //前k个人
	public Queue<People> knnQueue = new PriorityQueue<People>(k);//存放k个最近的人

	public List<People> trainList = new ArrayList<People>(); //这边一定要初始化
	public List<People> testList = new ArrayList<People>(); //不然在构造函数要初始化

	public static int errorNum = 0;//记录错误的个数
	public static int testNum;
	public static int trainNum;

	/**    
	 * 创建一个新的实例 Knn.    构造函数
	 *    
	 * @throws IOException    
	 */
	public Knn() {
		try {
			this.getTrainAndTestList();
			testNum = testList.size();
			trainNum = trainList.size();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**    
	 * 方法作用：  获取错误的比率
	 * @return      
	*/
	public double getErrorRate() {
		return (double) errorNum / (double) testNum;
	}

	/**    
	 * 方法作用：  获取正确分类的比率
	 * @return      
	*/
	public double getRightRate() {
		return 1.0 - (double) errorNum / (double) testNum;
	}

	/**    
	 * 方法作用：  开始对所有待测试的人进行分类，并获得错误分类数，便于后面计算概率
	 * @return      
	*/
	public void startClassify() {

		for (int i = 0; i < testList.size(); i++) { //遍历测试列表，即待分类列表
			this.judgePersonType(testList.get(i));
		}

	}

	/**    
	 * 方法作用：  判断一个待分类的人属于什么类别
	 * @return      
	*/
	public void judgePersonType(People needClassifyPerson) {
		int[] rates = new int[4]; //存放一个人分别是不被喜欢1，一般的被喜欢2，很受喜欢极具魅力3
		this.caculateDistance(needClassifyPerson); //每个待分类的人先调用这个函数，获得排序后的列表

		for (int i = 0; i < k; i++) {
			rates[trainList.get(i).getLikeLevelNum()]++; //遍历前k个列表，记录受喜欢的次数
		}
		int max = Utils.getMaxNumOfThree(rates[1], rates[2], rates[3]); //这里有bug，不是算三个数的最大值
		int maxIndex = -1; //记录最大值的索引下标
		for (int i = 1; i < rates.length; i++) {
			if (max == rates[i]) {
				maxIndex = i; //找到了就跳出循环
				break;
			}
		}
		if (maxIndex != needClassifyPerson.getLikeLevelNum()) { //如果分类跟测试集不一样，表示分类失败
			errorNum++; //错误数就要加1，因为分类失败
		}
		System.out.println("分类器分类后得出该人受喜欢程度为:" + maxIndex + ",实际上该人受喜欢的程度为:"
				+ needClassifyPerson.getLikeLevelNum());

	}

	/**    
	 * 方法作用：  输入一个人，判断其所属分类
	 * @return      
	*/
	public void judgeInputPersonType(People needClassifyPerson) {

		int[] rates = new int[4]; //存放一个人分别是不被喜欢1，一般的被喜欢2，很受喜欢极具魅力3
		this.caculateDistance(needClassifyPerson); //每个待分类的人先调用这个函数，获得排序后的列表

		for (int i = 0; i < k; i++) {
			rates[trainList.get(i).getLikeLevelNum()]++; //遍历前k个列表，记录受喜欢的次数
		}
		int max = Utils.getMaxNumOfThree(rates[1], rates[2], rates[3]); //这里有bug，不是算三个数的最大值
		int maxIndex = -1; //记录最大值的索引下标
		for (int i = 1; i < rates.length; i++) {
			if (max == rates[i]) {
				maxIndex = i; //找到了就跳出循环
				break;
			}
		}
		System.out.println("分类器分类后得出该人受喜欢程度为:" + maxIndex + "  ,  即       "
				+ Utils.getLikeLevelStr(maxIndex));

	}

	/**    
	 * 方法作用：  通过给定一个待分类的人，放入训练集中计算
	 * @return      
	*/
	@SuppressWarnings("unchecked")
	private void caculateDistance(People needClassifyPerson) {
		double f = needClassifyPerson.getFlyKm();
		double g = needClassifyPerson.getGamePercent();
		double ice = needClassifyPerson.getIceKg();

		for (int i = 0; i < trainList.size(); i++) {
			People p = trainList.get(i);
			double dis = Math.sqrt(Math.pow(f - p.getFlyKm(), 2) //计算欧氏距离
					+ Math.pow(g - p.getGamePercent(), 2)
					+ Math.pow(ice - p.getIceKg(), 2));
			trainList.get(i).setDistanceN(dis); //计算后的距离放置到  person属性中

		}
		ComparatorList com = new ComparatorList(); //比较器，用于列表排序
		Collections.sort(trainList, com);

	}

	/**    
	 * 方法作用：  创建测试列表和训练列表，从文件中读取1000个人的信息
	 * @return      
	*/
	private void getTrainAndTestList() throws IOException {
		BufferedReader br = new BufferedReader(new FileReader(
				Utils.getSrcPath("datingTestSet.txt")));//构造一个BufferedReader类来读取文件
		String s = null;
		while ((s = br.readLine()) != null) {
			trainList.add(new People(s));
		}
		br.close();
		Random random = new Random();
		int index = 0;
		for (int i = 0; i < 100; i++) { //随机选取100个人作为测试用
			index += random.nextInt(5); //每次从0-5里面随机选取
			testList.add(trainList.get(index)); //放入测试列表
			trainList.remove(index); //训练列表要移除该个人的信息爱
		}
	}

	public List<People> getTrainList() {
		return trainList;
	}

	public void setTrainList(List<People> trainList) {
		this.trainList = trainList;
	}

	public List<People> getTestList() {
		return testList;
	}

	public void setTestList(List<People> testList) {
		this.testList = testList;
	}

}
