package builder;

class AnimalCellBuilder extends CellBuilder{}

class AnimalBuilder {
    public void createAnimal(AnimalCellBuilder builder){
        builder.createNewCell();
        builder.createLysosomes();
        builder.createCellMembrane();
        builder.createCellNucleus();
        builder.createNuclearMembrane();
        builder.createCytoplasm();
        builder.createEndoplasmicReticulum();
        builder.createRibosomes();
        builder.createMitochondria();
        builder.createVacuoles();
    }
}