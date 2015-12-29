package cn.edu.hgd.knn;

/**     
 * 类名称：People    
 * 类描述：      个人信息类
 *     
 */
public class People {
	private double flyKm; //飞行的公里数
	private double gamePercent; //玩游戏所占的百分比
	private double iceKg; //吃冰淇淋千克数
	private String likeLevel; //受喜欢的程度
	private int likeLevelNum; //受喜欢程度的数值

	private double distanceN; //存放与测试数据的 欧式距离

	   
	/**    
	 * 创建一个新的实例 People.    
	 *    
	 * @param f
	 * @param g
	 * @param ice    
	 */
	public People(double f, double g, double ice) {
		this.flyKm = f;
		this.gamePercent = g;
		this.iceKg = ice;
	}

	/**    
	 * 创建一个新的实例 People.    
	 *    
	 * @param f
	 * @param g
	 * @param ice
	 * @param like
	 * @param dis    
	 */
	public People(double f, double g, double ice, int like, double dis) {
		this.flyKm = f;
		this.gamePercent = g;
		this.iceKg = ice;
		this.likeLevelNum = like;
		this.distanceN = dis;
	}

	/**    
	 * 创建一个新的实例 People.    
	 *    
	 * @param inputStr    
	 */
	public People(String inputStr) {
		String[] strs = inputStr.split("\\s+"); //从文件中读取的一行

		flyKm = Double.parseDouble(strs[0].trim()); //对字符串进行处理，分割出需要的数据放入对应的属性
		gamePercent = Double.parseDouble(strs[1].trim());
		iceKg = Double.parseDouble(strs[2].trim());
		likeLevel = strs[3].trim();
		if (likeLevel.equals("largeDoses")) { //极具有魅力，用数字3表示
			likeLevelNum = 3;
		} else if (likeLevel.equals("smallDoses")) { //一般魅力用2表示
			likeLevelNum = 2;
		} else {
			likeLevelNum = 1; //不受喜欢用1表示
		}

	}

	public People() {
	}

	public double getFlyKm() {
		return flyKm;
	}

	public void setFlyKm(double flyKm) {
		this.flyKm = flyKm;
	}

	public double getGamePercent() {
		return gamePercent;
	}

	public void setGamePercent(double gamePercent) {
		this.gamePercent = gamePercent;
	}

	public double getIceKg() {
		return iceKg;
	}

	public void setIceKg(double iceKg) {
		this.iceKg = iceKg;
	}

	public String getLikeLevel() {
		return likeLevel;
	}

	public void setLikeLevel(String likeLevel) {
		this.likeLevel = likeLevel;
	}

	public int getLikeLevelNum() {
		return likeLevelNum;
	}

	public void setLikeLevelNum(int likeLevelNum) {
		this.likeLevelNum = likeLevelNum;
	}

	public double getDistanceN() {
		return distanceN;
	}

	public void setDistanceN(double distanceN) {
		this.distanceN = distanceN;
	}

}
