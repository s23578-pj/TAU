import org.example.TriangleArea;
import static org.junit.Assert.assertTrue;
import org.junit.Test;
public class TriangleAreaTest {


    @Test
    public void testCanBuildTriangleWithValidSides() {
        assertTrue(TriangleArea.canBuildTriangle(3, 4, 5));
        assertTrue(TriangleArea.canBuildTriangle(7, 24, 25));
        assertTrue(TriangleArea.canBuildTriangle(5, 12, 13));
    }

    @Test
    public void testCannotBuildTriangleWithInvalidSides() {
        assertFalse(TriangleArea.canBuildTriangle(1, 1, 3));
        assertFalse(TriangleArea.canBuildTriangle(0, 0, 0));
    }

    @Test
    public void testCalculateTriangleArea() {
        assertEquals(6.0, TriangleArea.calculateTriangleArea(3, 4, 5), 0.001);
        assertEquals(84.0, TriangleArea.calculateTriangleArea(7, 24, 25), 0.001);
        assertEquals(30.0, TriangleArea.calculateTriangleArea(5, 12, 13), 0.001);
    }

    @Test
    public void testInvalidTriangleArea() {
        double invalidArea = TriangleArea.calculateTriangleArea(1, 1, 3);
        assertTrue(Double.isNaN(invalidArea));
    }

    @Test
    public void testInvalidSides() {
        assertFalse(TriangleArea.canBuildTriangle(-1, 2, 3));
        assertFalse(TriangleArea.canBuildTriangle(1, -2, 3));
        assertFalse(TriangleArea.canBuildTriangle(1, 2, -3));
    }

    @Test
    public void testZeroSides() {
        assertFalse(TriangleArea.canBuildTriangle(0, 1, 2));
        assertFalse(TriangleArea.canBuildTriangle(1, 0, 2));
        assertFalse(TriangleArea.canBuildTriangle(1, 2, 0));
    }

    @Test
    public void testEquilateralTriangle() {
        assertTrue(TriangleArea.canBuildTriangle(4, 4, 4));
        assertEquals(6.928, TriangleArea.calculateTriangleArea(4, 4, 4), 0.001);
    }

    @Test
    public void testIsoscelesTriangle() {
        assertTrue(TriangleArea.canBuildTriangle(5, 5, 7));
    }

    @Test
    public void testScaleneTriangle() {
        assertTrue(TriangleArea.canBuildTriangle(3, 4, 5));
    }
}
