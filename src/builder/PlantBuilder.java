package builder;

class PlantCellBuilder extends CellBuilder{
    public void createCellWall(){
        if(cell.getCellWall() == null)
            cell.setCellWall(new CellWall());
    }

    public void createChloroplasts(){
        cell.setChloroplasts(new Chloroplasts());
    }
}


class PlantBuilder {
    public void createPlant(PlantCellBuilder builder){
        builder.createNewCell();
        builder.createCellWall();
        builder.createLysosomes();
        builder.createChloroplasts();

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
