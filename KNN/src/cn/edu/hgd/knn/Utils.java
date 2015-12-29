package cn.edu.hgd.knn;

import java.io.File;
import java.net.URL;
import java.util.Comparator;

/**     
 * 类名称：Utils    
 * 类描述：     工具类
 *     
 */
public class Utils {

	/**    
	 * 方法作用：  计算三个数的最大值
	 * @return      
	*/
	public static int getMaxNumOfThree(int a, int b, int c) {
		int temp = Math.max(a, b);
		return Math.max(temp, c);
	}

	public static String getLikeLevelStr(int i) {
		if (i == 1) {
			return "didntLike";
		} else if (i == 2) {
			return "smallDoses";
		} else if (i == 3) {
			return "largeDoses";
		} else {
			return null;
		}
	}

	/* @param name   文件名  不包含路径
	 */
	public static String getSrcPath(String name) {
		String result = null;
		URL urlpath = Utils.class.getClassLoader().getResource(name);
		String path = urlpath.toString();
		
		if (path.startsWith("file")) {
			path = path.substring(5);
		}
		path.replace("/", File.separator);
		result = path;
		return result;

	}

}

/**     
 * 类名称：ComparatorList    
 * 类描述：    用于列表排序的比较
 *     
 */
@SuppressWarnings("rawtypes")
class ComparatorList implements Comparator {

	public int compare(Object arg0, Object arg1) {
		People p1 = (People) arg0;
		People p2 = (People) arg1;
		Double n1 = p1.getDistanceN();
		Double n2 = p2.getDistanceN();
		int flag = n1.compareTo(n2);
		return flag;

	}
}
