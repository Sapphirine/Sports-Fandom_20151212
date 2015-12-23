package Test.BigData;
import java.io.File;
import java.util.*;

import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.ItemBasedRecommender;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.Recommender;
import org.apache.mahout.cf.taste.recommender.UserBasedRecommender;
import org.apache.mahout.cf.taste.recommender.slopeone.DiffStorage;
import org.apache.mahout.cf.taste.similarity.ItemSimilarity;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;
import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.common.Weighting;
import org.apache.mahout.cf.taste.eval.IRStatistics;
import org.apache.mahout.cf.taste.eval.RecommenderBuilder;
import org.apache.mahout.cf.taste.eval.RecommenderEvaluator;
import org.apache.mahout.cf.taste.eval.RecommenderIRStatsEvaluator;
import org.apache.mahout.cf.taste.impl.eval.AverageAbsoluteDifferenceRecommenderEvaluator;
import org.apache.mahout.cf.taste.impl.eval.GenericRecommenderIRStatsEvaluator;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.neighborhood.NearestNUserNeighborhood;
import org.apache.mahout.cf.taste.impl.neighborhood.ThresholdUserNeighborhood;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.CachingUserSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.EuclideanDistanceSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.LogLikelihoodSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.PearsonCorrelationSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.SpearmanCorrelationSimilarity;
import org.apache.mahout.cf.taste.impl.similarity.TanimotoCoefficientSimilarity;
import org.apache.mahout.cf.taste.impl.recommender.GenericItemBasedRecommender;
import org.apache.mahout.cf.taste.impl.recommender.knn.KnnItemBasedRecommender;
import org.apache.mahout.cf.taste.impl.recommender.knn.NonNegativeQuadraticOptimizer;
//import com.sun.xml.bind.v2.schemagen.xmlschema.List;
import org.apache.mahout.cf.taste.impl.recommender.knn.Optimizer;
import org.apache.mahout.cf.taste.impl.recommender.slopeone.MemoryDiffStorage;
import org.apache.mahout.cf.taste.impl.recommender.slopeone.SlopeOneRecommender;
import org.apache.mahout.cf.taste.impl.recommender.svd.ALSWRFactorizer;
import org.apache.mahout.cf.taste.impl.recommender.svd.SVDRecommender;
import org.apache.mahout.common.RandomUtils;

public class Rec {
	public static void main(String[] args) throws Exception {

		/* read in list of users */
        BufferedReader in = new BufferedReader(new FileReader("user_ids"));
        String str;
        List<String> list = new ArrayList<String>();
        while((str = in.readLine()) != null){
            list.add(str);
        }
        String[] users = list.toArray(new String[0]);

        /* set up file to write to */
		File fout = new File("recs.txt");
		FileOutputStream fos = new FileOutputStream(fout);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));

		/* build model and recommend */
		RandomUtils.useTestSeed();
		DataModel model = new FileDataModel (new File("/Users/qiansheng/Desktop/user_convert.txt"));
		//DataModel model = new FileDataModel (new File("/Users/qiansheng/Downloads/Webscope_R4/ydata-ymovies-user-movie-ratings-train-v1_0.txt"));
	    //DiffStorage diffStorage = new MemoryDiffStorage(model, Weighting.UNWEIGHTED, Long.MAX_VALUE);
	    //SlopeOneRecommender recommender = new SlopeOneRecommender(model,Weighting.UNWEIGHTED,Weighting.UNWEIGHTED,diffStorage);
		UserSimilarity similarity = new PearsonCorrelationSimilarity(model); 
		//UserSimilarity similarity = new LogLikelihoodSimilarity(model); 
		//UserNeighborhood neighborhood =new ThresholdUserNeighborhood(2, similarity, model);
		UserNeighborhood neighborhood = new NearestNUserNeighborhood(10, similarity, model);
		UserBasedRecommender recommender = new GenericUserBasedRecommender(model, neighborhood, similarity);
		//System.out.println(recommender);
		System.out.println("--------recommendations--------");
		for(String string_id : users){
			int user_id = Integer.parseInt(string_id);
		    List<RecommendedItem> recommendations = recommender.recommend(user_id, 1);
		    //List<RecommendedItem> recommendations = recommender.recommend(4, 1);
		    //System.out.println(recommendations);
		
		    for (RecommendedItem recommendation : recommendations) {
		    	/* write recommendation to file */
		    	bw.write(recommendation);
		    	bw.newLine();
			    System.out.println(recommendation);
		    }
		}
	 
		bw.close();

//		RecommenderEvaluator evaluator = new AverageAbsoluteDifferenceRecommenderEvaluator (); 
//		RecommenderIRStatsEvaluator irevaluator = new GenericRecommenderIRStatsEvaluator ();
//		RecommenderBuilder recommenderBuilder = new RecommenderBuilder() {
//		@Override
//		  public Recommender buildRecommender(DataModel model) throws TasteException {
//			ItemSimilarity similarity = new LogLikelihoodSimilarity(model); 
//			Optimizer optimizer = new NonNegativeQuadraticOptimizer();
//			return new KnnItemBasedRecommender(model, similarity, optimizer, 10);
//		} };
//		double score = evaluator.evaluate(recommenderBuilder, null, model, 0.95, 0.05);
//		System.out.println("--------score--------");
//		System.out.println(score);

	}

}

