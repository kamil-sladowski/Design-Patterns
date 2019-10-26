package builder;

public class Main {

    public static void main(String[] args) {
	    PlantCellBuilder plantCellBuilder = new PlantCellBuilder();
        AnimalCellBuilder animalCellBuilder = new AnimalCellBuilder();

        PlantBuilder plantBuilder = new PlantBuilder();
	    AnimalBuilder animalBuilder = new AnimalBuilder();

	    plantBuilder.createPlant(plantCellBuilder);
	    animalBuilder.createAnimal(animalCellBuilder);
    }
}
