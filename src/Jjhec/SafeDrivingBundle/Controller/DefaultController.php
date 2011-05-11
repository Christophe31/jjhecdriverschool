<?php

namespace Jjhec\SafeDrivingBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

class DefaultController extends Controller
{
    public function indexAction()
    {
        return $this->render('JjhecSafeDrivingBundle:Default:index.html.twig',array("text"=>"value"));
    }

    /**
     * @extra:Route("/hello/{name}", name="default.hello")
     * @extra:Template()
     */
    public function helloAction($name)
    {
        return array('name' => $name);
    }

    /**
     * @extra:Route("/prefix/{var1}/{var2}", name="default.hello", requirements = {"var2" = "\d+"})
     * @extra:Template("JjhecSafeDrivingBundle:DefaultController:helloAction")
     * @extra:Secure(roles="Group")
     * @extra:Cache(expires="+2 days")
     */
     public function specificHelloAction($var1, $var2)
     {
         return array('name' => $var1.($var2+2));
     }
}
