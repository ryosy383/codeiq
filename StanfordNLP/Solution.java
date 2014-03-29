import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Properties;

import edu.stanford.nlp.ling.CoreAnnotations.LemmaAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.SentencesAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TokensAnnotation;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.util.CoreMap;

public class Solution {

	protected StanfordCoreNLP pipeline;
	//Propertiesの設定
	public Solution() {
		Properties props;
		props = new Properties();
		props.put("annotators", "tokenize, ssplit, pos, lemma");
		props.setProperty("tokenize.options", "tokenizeNLs=true,normalizeSpace=false,unicodeEllipsis=true,ptb3Escaping=false");
		this.pipeline = new StanfordCoreNLP(props);
	}

	/**
	 * 文字列を原形に変換して、その要素数をカウントする.
	 * @param documentText 対象の文字列
	 * @return HashMap<String, Integer> 要素と要素数
	 */
	public HashMap<String, Integer> lemmasCount(String documentText) {
		HashMap<String, Integer> lemmas = new HashMap<String, Integer>();
		Annotation document = new Annotation(documentText);
		this.pipeline.annotate(document);
		List<CoreMap> sentences = document.get(SentencesAnnotation.class);
		for (CoreMap sentence : sentences) {
			for (CoreLabel token : sentence.get(TokensAnnotation.class)) {
				String s = token.get(LemmaAnnotation.class).toLowerCase();
				if (s.length() <= 3) {
					//3文字以下の単語は、ノイズとして切り捨て
					continue;
				}
				int count;
				if (lemmas.containsKey(s)) {
					count = lemmas.get(s);
				} else {
					count = 0;
				}
				count++;
				lemmas.put(s, count);
			}
		}
		return lemmas;
	}

	public static void main(String[] args) {

		//ファイルの読み込み
		StringBuffer sb = new StringBuffer("");
		FileReader in = null;
		BufferedReader br = null;
		try {
			in = new FileReader("rfc2616.txt");
			br = new BufferedReader(in);
			String line;
			while ((line = br.readLine()) != null) {
				sb.append(line);
				sb.append(System.getProperty("line.separator"));
			}
		} catch (IOException e) {
			System.out.println(e);
		} finally {
			if (br != null) {
				try {
					br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			if (in != null) {
				try {
					in.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}

		Solution solution = new Solution();
		HashMap<String, Integer> lemmas = solution.lemmasCount(sb.toString());
		//降順にソート
		List<Map.Entry<String, Integer>> entries =
				new ArrayList<Map.Entry<String, Integer>>(lemmas.entrySet());
		Collections.sort(entries, new Comparator<Map.Entry<String, Integer>>() {

			@Override
			public int compare(
					Entry<String, Integer> entry1, Entry<String, Integer> entry2) {
				return ((Integer) entry2.getValue()).compareTo((Integer) entry1.getValue());
			}
		});
		// 内容TOP10を表示
		for (int i = 0; i < 10 && i < entries.size(); i++) {
			System.out.println(entries.get(i).getKey());
		}

	}
}
