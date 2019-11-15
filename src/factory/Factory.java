package factory;

import com.google.gson.Gson;

import java.util.ArrayList;
import java.util.Arrays;

class ClassToSerialize{
    public String text1;
    public String text2;
    public Integer value1;
    public ArrayList<String> values2;

    public ClassToSerialize(String text1, String text2, Integer value1, ArrayList<String> values2) {
        this.text1 = text1;
        this.text2 = text2;
        this.value1 = value1;
        this.values2 = values2;
    }

    @Override
    public String toString() {
        return "ClassToSerialize{" +
                "text1='" + text1 + '\'' +
                ", text2='" + text2 + '\'' +
                ", value1=" + value1 +
                ", values2=" + values2 +
                '}';
    }

    public void setText1(String text1) {
        this.text1 = text1;
    }

    public void setText2(String text2) {
        this.text2 = text2;
    }

    public void setValue1(Integer value1) {
        this.value1 = value1;
    }

    public void setValues2(ArrayList<String> values2) {
        this.values2 = values2;
    }

    public String getText1() {
        return text1;
    }

    public String getText2() {
        return text2;
    }

    public Integer getValue1() {
        return value1;
    }

    public ArrayList<String> getValues2() {
        return values2;
    }
}

abstract class Plugin{
    abstract public String serialize(ClassToSerialize obj);
    abstract public ClassToSerialize deserialize(String str);
}

class JSONPlugin extends Plugin{
    @Override
    public String serialize(ClassToSerialize obj) {
        System.out.println("JSON");
        Gson gson = new Gson();
        String json = gson.toJson(obj);
        return json;
    }

    @Override
    public ClassToSerialize deserialize(String json) {
        ClassToSerialize obj = new Gson().fromJson(json, ClassToSerialize.class);
        return obj;
    }
}

class XMLPlugin extends Plugin{
    @Override
    public String serialize(ClassToSerialize obj) {
        System.out.println("XML");
        return "<obj><text1>" + obj.text1 + "</text1>" +
                "<text2>" + obj.text2 + "</text2>" +
                "<value1>" + obj.value1.toString() + "</value1>" +
                "<val2>" + obj.values2.get(0) + ", " + obj.values2.get(1) +"</val2></obj>";

    }

    @Override
    public ClassToSerialize deserialize(String str) {
        str = str.replace("</text1>", ";");
        str = str.replace("<obj><text1>", "");
        str = str.replace("</text2>", ";");
        str = str.replace("<text2>", "");
        str = str.replace("</value1>", ";");
        str = str.replace("<value1>", "");
        str = str.replace("</val2></obj>", ";");
        str = str.replace("<val2>", "");
        String[] x = str.split(";");
        return new ClassToSerialize(
                x[0], x[1], Integer.valueOf(x[2]), new ArrayList<>(Arrays.asList(x[3].split(","))));
    }
}

class CSVPlugin extends Plugin{
    @Override
    public String serialize(ClassToSerialize obj) {
        System.out.println("CSV");
        return obj.text1 + ";" + obj.text2 + ";" + obj.value1.toString() + ";" + obj.values2.get(0) + "; " + obj.values2.get(1) + "\n";
    }

    @Override
    public ClassToSerialize deserialize(String str) {
        System.out.println(str);
        String[] splited = str.split(";");
        System.out.println(splited[2]);
        return new ClassToSerialize(
                splited[0], splited[1], Integer.valueOf(splited[2]),
                new ArrayList<>(Arrays.asList(splited[3], splited[4])));
    }
}


abstract class AbstractSerializer {
    abstract Plugin createPlugin();
}

class JsonSerializer extends AbstractSerializer{
    public JsonSerializer() {
    }

    @Override
    Plugin createPlugin() {
        return new JSONPlugin();
    }
}

class XmlSerializer extends AbstractSerializer{

    @Override
    Plugin createPlugin() {
        return new XMLPlugin();
    }
}

class CSVserializer extends AbstractSerializer{

    @Override
    Plugin createPlugin() {
        return new CSVPlugin();
    }
}


public class Factory {
    public static void main(String[] args) {
        ArrayList<String> values2 = new ArrayList<>();
        values2.add("AAA");
        values2.add("BBB");

        AbstractSerializer [] serializers = new AbstractSerializer[3];
        serializers[2] = new JsonSerializer();
        serializers[1] = new XmlSerializer();
        serializers[0] = new CSVserializer();
        ClassToSerialize objToSerialize = new ClassToSerialize("XXX", "YYY", 123, values2);


        for(AbstractSerializer serializer : serializers){
            Plugin p = serializer.createPlugin();
            String str = p.serialize(objToSerialize);
            System.out.println("Serialized:");
            System.out.println(str);
            System.out.println("Deserialized:");
            System.out.println(p.deserialize(str).toString());
        }
    }
}
